import os
import yaml
import nbformat

def get_md_metadata(filepath):
    """Lit le front matter d'un fichier .md de manière souple"""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    start = content.find("---")
    if start != -1:
        end = content.find("---", start + 3)
        if end != -1:
            try:
                res = yaml.safe_load(content[start+3:end])
                return res if isinstance(res, dict) else {}
            except:
                return {}
    return {}

def get_ipynb_metadata(filepath):
    """
    Lit le front matter dans la première cellule contenant des tirets.
    Capable de lire le YAML même s'il est caché dans une balise HTML.
    """
    try:
        nb = nbformat.read(filepath, as_version=4)
        for cell in nb.cells:
            if cell.cell_type in ["raw", "markdown"]:
                source = cell.source
                start = source.find("---")
                if start != -1:
                    end = source.find("---", start + 3)
                    if end != -1:
                        try:
                            parsed = yaml.safe_load(source[start+3:end])
                            if isinstance(parsed, dict) and "title" in parsed:
                                return parsed
                        except:
                            pass
    except:
        return {}
    return {}

def get_items(docs_dir, subfolder):
    """Filtre les brouillons et extrait les métadonnées."""
    folder = os.path.join(docs_dir, subfolder)
    items = []
    if not os.path.exists(folder):
        return items

    for filename in sorted(os.listdir(folder)):
        if filename in ["index.md", ".pages"]:
            continue
            
        if filename.startswith("_"):
            continue

        filepath = os.path.join(folder, filename)
        meta = {}

        if filename.endswith(".md"):
            meta = get_md_metadata(filepath)
            meta["_file"] = filename.replace(".md", "")
            meta["_notebook"] = False

        elif filename.endswith(".ipynb"):
            meta = get_ipynb_metadata(filepath)
            meta["_file"] = filename.replace(".ipynb", "")
            meta["_notebook"] = True

        else:
            continue

        if meta and meta.get("title"):
            items.append(meta)

    items.sort(key=lambda x: str(x.get("date", "") or ""), reverse=True)
    return items

def define_env(env):
    docs_dir = env.conf["docs_dir"]

    @env.macro
    def render_apps():
        items = get_items(docs_dir, os.path.join("app", "apps"))
        return _render_cards(items, "apps")

    @env.macro
    def render_projects():
        items = get_items(docs_dir, os.path.join("project", "projects"))
        return _render_cards(items, "projects")

def _render_cards(items, section):
    """Génère la grille de cartes."""
    if not items:
        return "<p><em>Aucun élément pour l'instant.</em></p>"

    cards = []

    for item in items:
        title       = item.get("title", "")
        description = item.get("description", "")
        tags        = item.get("tags", [])
        status      = item.get("status", "")
        image       = item.get("image", "") or ""
        file_slug   = item.get("_file", "")
        notebook    = item.get("_notebook", False)

        if image:
            img_line = f"![{title}]({image})"
        elif section == "apps":
            if notebook:
                img_line = "![](../app/assets/placeholder-notebook.png)"
            else:
                img_line = "![](../app/assets/placeholder-project.png)"
        else:
            if notebook:
                img_line = "![](../assets/images/placeholder-notebook.png)"
            else:
                img_line = "![](../assets/images/placeholder-project.png)"

        status_colors = {
            "terminé":  ("#d4edda", "#155724", "✓ Terminé"),
            "en cours": ("#fff3cd", "#856404", "⟳ En cours"),
            "idée":     ("#e2e3e5", "#383d41", "✦ Idée"),
        }
        sc = status_colors.get(status.lower()) if status else None
        status_badge = (
            f'<span style="font-size:0.75rem;font-weight:600;padding:2px 8px;'
            f'border-radius:12px;background:{sc[0]};color:{sc[1]}">{sc[2]}</span>'
        ) if sc else ""

        notebook_badge = (
            '<span style="font-size:0.75rem;font-weight:600;padding:2px 8px;'
            'border-radius:12px;background:#e6f1fb;color:#185fa5;margin-left:4px">'
            '📓 Notebook</span>'
        ) if notebook else ""

        badges = f"{status_badge}{notebook_badge}" if (status_badge or notebook_badge) else ""
        tags_str = " ".join([f"`{t}`" for t in tags]) if tags else ""

        ext = ".ipynb" if notebook else ".md"
        if section == "projects":
            href = f"projects/{file_slug}{ext}"
        elif section == "apps":
            href = f"apps/{file_slug}{ext}"
        else:
            href = f"{file_slug}{ext}"
            
        btn_label = "Ouvrir le Notebook →" if notebook else "Lire →"

        card = f"""<div class="project-card" markdown>
{img_line}

{badges}

**{title}**

{description}

{tags_str}

[{btn_label}]({href}){{ .md-button }}
</div>"""

        cards.append(card)

    return '<div class="grid" markdown>\n\n' + "\n\n".join(cards) + "\n\n</div>"