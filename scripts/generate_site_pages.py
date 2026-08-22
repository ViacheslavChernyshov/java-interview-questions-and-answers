from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
REPOSITORY_URL = "https://github.com/ViacheslavChernyshov/java-interview-questions-and-answers"
LANGUAGES = {
    "eng": {
        "lang_code": "en",
        "site_prefix": "",
        "output_dir": DOCS_DIR / "questions",
        "source_dir": REPO_ROOT / "eng",
        "label": "English",
        "library_title": "Java Interview Questions and Answers Library",
        "library_description": "Browse 500+ Java interview answers directly on the site across Spring Boot, SQL, Hibernate, Kafka, Concurrency, and other backend topics.",
        "home_url": "/",
    },
    "ru": {
        "lang_code": "ru",
        "site_prefix": "ru",
        "output_dir": DOCS_DIR / "ru" / "questions",
        "source_dir": REPO_ROOT / "ru",
        "label": "Russian",
        "library_title": "Java interview questions и ответы на сайте",
        "library_description": "Полная библиотека ответов по Java interview: Spring Boot, SQL, Hibernate, Kafka, многопоточность, Docker, Kubernetes и другие backend-темы.",
        "home_url": "/ru/",
    },
    "ua": {
        "lang_code": "uk",
        "site_prefix": "uk",
        "output_dir": DOCS_DIR / "uk" / "questions",
        "source_dir": REPO_ROOT / "ua",
        "label": "Ukrainian",
        "library_title": "Java interview questions і відповіді на сайті",
        "library_description": "Повна бібліотека відповідей для Java interview: Spring Boot, SQL, Hibernate, Kafka, багатопоточність, Docker, Kubernetes та інші backend-теми.",
        "home_url": "/uk/",
    },
}

LOCALIZED_TEXT = {
    "eng": {
        "library_intro": "Browse the full answer library directly on the site in English. Every section and question page is generated from the source Markdown files in the repository, so the site and GitHub content stay in sync.",
        "library_use_heading": "How to use this library",
        "library_steps": [
            "Pick one topic cluster that matches the role you are targeting.",
            "Open the section page to see the full question sequence.",
            "Read the answer page directly on the site, then switch languages or jump to the next question.",
        ],
        "library_sections_heading": "All sections",
        "table_topic": "Topic",
        "table_questions": "Questions",
        "section_questions_heading": "Questions in this section",
        "section_navigator_heading": "Study navigator",
        "section_description": "{count} interview questions and answers in the {label} section.",
    },
    "ru": {
        "library_intro": "Открывайте полную библиотеку ответов прямо на сайте на русском языке. Каждая секция и каждая страница вопроса генерируются из исходных Markdown-файлов репозитория, поэтому сайт и GitHub-версия остаются синхронизированными.",
        "library_use_heading": "Как пользоваться этой библиотекой",
        "library_steps": [
            "Выберите тематический блок под роль, на которую готовитесь.",
            "Откройте страницу секции, чтобы пройти все вопросы по порядку.",
            "Читайте ответ прямо на сайте, затем переключайте язык или переходите к следующему вопросу.",
        ],
        "library_sections_heading": "Все разделы",
        "table_topic": "Тема",
        "table_questions": "Вопросы",
        "section_questions_heading": "Вопросы этого раздела",
        "section_navigator_heading": "Навигатор по разделу",
        "section_description": "{count} вопросов и ответов в разделе {label}.",
    },
    "ua": {
        "library_intro": "Відкривайте повну бібліотеку відповідей прямо на сайті українською. Кожна секція і кожна сторінка питання генеруються з вихідних Markdown-файлів репозиторію, тому сайт і GitHub-версія залишаються синхронізованими.",
        "library_use_heading": "Як користуватися цією бібліотекою",
        "library_steps": [
            "Оберіть тематичний блок під роль, до якої готуєтесь.",
            "Відкрийте сторінку секції, щоб пройти всі питання по порядку.",
            "Читайте відповідь прямо на сайті, потім перемикайте мову або переходьте до наступного питання.",
        ],
        "library_sections_heading": "Усі розділи",
        "table_topic": "Тема",
        "table_questions": "Питання",
        "section_questions_heading": "Питання цього розділу",
        "section_navigator_heading": "Навігатор по розділу",
        "section_description": "{count} питань і відповідей у розділі {label}.",
    },
}

SECTION_RE = re.compile(r"^(?P<number>\d+)\.\s+(?P<label>.+)$")
QUESTION_RE = re.compile(r"^(?P<number>\d+)\.\s+(?P<label>.+)\.md$")
FRONT_MATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


@dataclass
class Question:
    number: int
    title: str
    file_name: str
    source_path: Path
    source_relative_path: str
    body: str
    summary: str
    position: int = 0
    slug: str = ""
    url: str = ""
    prev_title: str = ""
    prev_url: str = ""
    next_title: str = ""
    next_url: str = ""


@dataclass
class Section:
    number: int
    label: str
    dir_name: str
    source_dir: Path
    navigator_path: Path
    navigator_body: str
    navigator_title: str
    slug: str = ""
    url: str = ""
    questions: list[Question] = field(default_factory=list)


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def render_front_matter(data: dict) -> str:
    lines: list[str] = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append("  -")
                for nested_key, nested_value in item.items():
                    lines.append(f"    {nested_key}: {yaml_quote(str(nested_value))}")
            continue
        if isinstance(value, int):
            lines.append(f"{key}: {value}")
            continue
        lines.append(f"{key}: {yaml_quote(str(value))}")
    lines.append("---")
    return "\n".join(lines)


def slugify(text: str) -> str:
    ascii_replacements = {
        "@": " at ",
        "&": " and ",
        "+": " plus ",
        "/": " ",
        "_": " ",
        "'": "",
    }
    normalized = text.lower()
    for source, target in ascii_replacements.items():
        normalized = normalized.replace(source, target)
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized).strip("-")
    return normalized or "item"


def parse_numbered_name(name: str, pattern: re.Pattern[str]) -> tuple[int, str]:
    match = pattern.match(name)
    if not match:
        raise ValueError(f"Unsupported numbered name: {name}")
    return int(match.group("number")), match.group("label")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def split_heading(markdown: str, fallback_title: str) -> tuple[str, str]:
    text = FRONT_MATTER_RE.sub("", markdown, count=1)
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        body = "\n".join(lines[1:]).lstrip("\n")
        return title, body
    return fallback_title, text.strip()


def extract_summary(body: str) -> str:
    paragraphs: list[str] = []
    inside_code = False
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if line.startswith("```"):
            inside_code = not inside_code
            continue
        if inside_code or not line:
            if paragraphs:
                break
            continue
        if line.startswith(("#", "-", "*", "|", ">", "1.", "2.", "3.")):
            continue
        paragraphs.append(line)
    summary = " ".join(paragraphs) if paragraphs else "Structured Java interview answer with junior, middle, and senior-level explanation."
    summary = re.sub(r"`([^`]*)`", r"\1", summary)
    summary = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", summary)
    summary = summary.replace("**", "").replace("__", "").replace("*", "")
    summary = re.sub(r"\s+", " ", summary).strip()
    if len(summary) <= 180:
        return summary
    return summary[:177].rstrip() + "..."


def relative_question_link(question_slug: str) -> str:
    return f"./{question_slug}/"


def relative_section_link(section_slug: str) -> str:
    return f"./{section_slug}/"


def site_url(lang_key: str, *parts: str) -> str:
    prefix = LANGUAGES[lang_key]["site_prefix"]
    clean_parts = [part.strip("/") for part in parts if part]
    if prefix:
        return "/" + "/".join([prefix, *clean_parts]) + "/"
    return "/" + "/".join(clean_parts) + "/" if clean_parts else "/"


def rewrite_navigator_links(navigator_body: str, section: Section) -> str:
    rewritten = navigator_body
    for question in section.questions:
        replacement = relative_question_link(question.slug)
        candidates = {
            question.file_name,
            quote(question.file_name),
            question.file_name.replace(" ", "%20"),
        }
        for candidate in candidates:
            rewritten = rewritten.replace(f"]({candidate})", f"]({replacement})")
    return rewritten


def parse_language(lang_key: str) -> dict[int, Section]:
    source_dir: Path = LANGUAGES[lang_key]["source_dir"]
    sections: dict[int, Section] = {}

    for entry in sorted(source_dir.iterdir(), key=lambda item: item.name):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        try:
            number, label = parse_numbered_name(entry.name, SECTION_RE)
        except ValueError:
            continue

        navigator_candidates = sorted(entry.glob("00.*.md"))
        if not navigator_candidates:
            raise FileNotFoundError(f"Navigator file not found in {entry}")
        navigator_path = navigator_candidates[0]
        navigator_title, navigator_body = split_heading(read_text(navigator_path), label)

        questions: list[Question] = []
        for file_path in sorted(entry.glob("*.md"), key=lambda item: item.name):
            if file_path.name.startswith(("00.", "_")):
                continue
            try:
                question_number, fallback_title = parse_numbered_name(file_path.name, QUESTION_RE)
            except ValueError:
                continue
            title, body = split_heading(read_text(file_path), fallback_title)
            source_relative = file_path.relative_to(REPO_ROOT).as_posix()
            questions.append(
                Question(
                    number=question_number,
                    title=title,
                    file_name=file_path.name,
                    source_path=file_path,
                    source_relative_path=source_relative,
                    body=body.strip(),
                    summary=extract_summary(body),
                )
            )

        questions.sort(key=lambda question: question.number)
        for position, question in enumerate(questions, start=1):
            question.position = position
        sections[number] = Section(
            number=number,
            label=label,
            dir_name=entry.name,
            source_dir=entry,
            navigator_path=navigator_path,
            navigator_body=navigator_body.strip(),
            navigator_title=navigator_title,
            questions=questions,
        )

    return sections


def assign_shared_slugs(all_sections: dict[str, dict[int, Section]]) -> None:
    english_sections = all_sections["eng"]
    for section_number in sorted(english_sections):
        section = english_sections[section_number]
        section.slug = f"{section.number:02d}-{slugify(section.label)}"
        section.url = site_url("eng", "questions", section.slug)
        for question in section.questions:
            question.slug = f"{question.position:02d}-{slugify(question.title)}"
            question.url = site_url("eng", "questions", section.slug, question.slug)

    for lang_key, sections in all_sections.items():
        if lang_key == "eng":
            continue
        for section_number in sorted(sections):
            section = sections[section_number]
            english_section = english_sections[section_number]
            section.slug = english_section.slug
            section.url = site_url(lang_key, "questions", section.slug)
            for index, question in enumerate(section.questions):
                if index < len(english_section.questions):
                    english_question = english_section.questions[index]
                    question.position = english_question.position
                    question.slug = english_question.slug
                else:
                    question.position = index + 1
                    question.slug = f"{question.position:02d}-{slugify(question.title)}"
                question.url = site_url(lang_key, "questions", section.slug, question.slug)


def assign_prev_next(section: Section) -> None:
    for index, question in enumerate(section.questions):
        if index > 0:
            previous_question = section.questions[index - 1]
            question.prev_title = previous_question.title
            question.prev_url = previous_question.url
        if index + 1 < len(section.questions):
            next_question = section.questions[index + 1]
            question.next_title = next_question.title
            question.next_url = next_question.url


def build_alternates(all_sections: dict[str, dict[int, Section]], section_number: int, question_position: int | None = None) -> list[dict[str, str]]:
    alternates: list[dict[str, str]] = []
    default_url = all_sections["eng"][section_number].url
    for lang_key, lang_config in LANGUAGES.items():
        section = all_sections[lang_key][section_number]
        if question_position is None:
            url = section.url
        else:
            question_map = {question.position: question for question in section.questions}
            if question_position not in question_map:
                continue
            url = question_map[question_position].url
            if lang_key == "eng":
                default_url = url
        if question_position is None and lang_key == "eng":
            default_url = url
        alternates.append({"lang": lang_config["lang_code"], "url": url})
    alternates.append({"lang": "x-default", "url": default_url})
    return alternates


def build_library_alternates() -> list[dict[str, str]]:
    alternates = []
    for lang_key, lang_config in LANGUAGES.items():
        alternates.append({"lang": lang_config["lang_code"], "url": site_url(lang_key, "questions")})
    alternates.append({"lang": "x-default", "url": site_url("eng", "questions")})
    return alternates


def build_library_content(lang_key: str, sections: Iterable[Section]) -> str:
    lang = LANGUAGES[lang_key]
    text = LOCALIZED_TEXT[lang_key]
    lines = [
        f"# {lang['library_title']}",
        "",
        text["library_intro"],
        "",
        f"## {text['library_use_heading']}",
        "",
    ]
    for step in text["library_steps"]:
        lines.append(f"- {step}")
    lines.extend([
        "",
        f"## {text['library_sections_heading']}",
        "",
        f"| # | {text['table_topic']} | {text['table_questions']} |",
        "| --- | --- | --- |",
    ])
    for section in sections:
        lines.append(f"| {section.number} | [{section.label}]({relative_section_link(section.slug)}) | {len(section.questions)} |")
    return "\n".join(lines) + "\n"


def build_section_content(lang_key: str, section: Section) -> str:
    text = LOCALIZED_TEXT[lang_key]
    rewritten_navigator = rewrite_navigator_links(section.navigator_body, section)
    lines = [
        f"## {text['section_questions_heading']}",
        "",
    ]
    for question in section.questions:
        lines.append(f"{question.position}. [{question.title}]({relative_question_link(question.slug)})")
    lines.extend([
        "",
        f"## {text['section_navigator_heading']}",
        "",
        rewritten_navigator,
        "",
    ])
    return "\n".join(lines)


def build_question_content(question: Question) -> str:
    return question.body.strip() + "\n"


def ensure_clean_output() -> None:
    targets = [
        DOCS_DIR / "questions",
        DOCS_DIR / "ru" / "questions",
        DOCS_DIR / "uk" / "questions",
    ]
    for target in targets:
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)


def write_page(path: Path, front_matter: dict, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    page = render_front_matter(front_matter) + "\n\n" + content.strip() + "\n"
    path.write_text(page, encoding="utf-8")


def build_question_front_matter(lang_key: str, section: Section, question: Question, all_sections: dict[str, dict[int, Section]]) -> dict:
    lang = LANGUAGES[lang_key]
    return {
        "layout": "content-page",
        "kind": "question",
        "title": question.title,
        "description": question.summary,
        "lang": lang["lang_code"],
        "language_label": lang["label"],
        "home_url": lang["home_url"],
        "library_url": site_url(lang_key, "questions"),
        "section_title": section.label,
        "section_url": section.url,
        "section_number": section.number,
        "question_number": question.position,
        "source_url": f"{REPOSITORY_URL}/blob/master/{question.source_relative_path}",
        "prev_title": question.prev_title,
        "prev_url": question.prev_url,
        "next_title": question.next_title,
        "next_url": question.next_url,
        "alternates": build_alternates(all_sections, section.number, question.position),
    }


def build_section_front_matter(lang_key: str, section: Section, all_sections: dict[str, dict[int, Section]]) -> dict:
    lang = LANGUAGES[lang_key]
    text = LOCALIZED_TEXT[lang_key]
    source_relative = section.navigator_path.relative_to(REPO_ROOT).as_posix()
    return {
        "layout": "content-page",
        "kind": "section",
        "title": section.label,
        "description": text["section_description"].format(count=len(section.questions), label=section.label),
        "lang": lang["lang_code"],
        "language_label": lang["label"],
        "home_url": lang["home_url"],
        "library_url": site_url(lang_key, "questions"),
        "section_title": section.label,
        "section_url": section.url,
        "section_number": section.number,
        "question_count": len(section.questions),
        "source_url": f"{REPOSITORY_URL}/blob/master/{source_relative}",
        "alternates": build_alternates(all_sections, section.number),
    }


def build_library_front_matter(lang_key: str) -> dict:
    lang = LANGUAGES[lang_key]
    return {
        "layout": "content-page",
        "kind": "library",
        "title": lang["library_title"],
        "description": lang["library_description"],
        "lang": lang["lang_code"],
        "language_label": lang["label"],
        "home_url": lang["home_url"],
        "library_url": site_url(lang_key, "questions"),
        "alternates": build_library_alternates(),
    }


def generate_pages(all_sections: dict[str, dict[int, Section]]) -> None:
    ensure_clean_output()

    for lang_key, sections in all_sections.items():
        ordered_sections = [sections[number] for number in sorted(sections)]

        for section in ordered_sections:
            assign_prev_next(section)

        output_dir: Path = LANGUAGES[lang_key]["output_dir"]

        write_page(
            output_dir / "index.md",
            build_library_front_matter(lang_key),
            build_library_content(lang_key, ordered_sections),
        )

        for section in ordered_sections:
            write_page(
                output_dir / section.slug / "index.md",
                build_section_front_matter(lang_key, section, all_sections),
                build_section_content(lang_key, section),
            )
            for question in section.questions:
                write_page(
                    output_dir / section.slug / question.slug / "index.md",
                    build_question_front_matter(lang_key, section, question, all_sections),
                    build_question_content(question),
                )


def main() -> None:
    all_sections = {lang_key: parse_language(lang_key) for lang_key in LANGUAGES}
    assign_shared_slugs(all_sections)
    generate_pages(all_sections)

    total_questions = sum(len(section.questions) for section in all_sections["eng"].values())
    print(
        f"Generated {total_questions} question pages per language across "
        f"{len(all_sections['eng'])} sections."
    )


if __name__ == "__main__":
    main()
