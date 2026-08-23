import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const REPO_ROOT = path.resolve(__dirname, '..');
const DOCS_DIR = path.join(REPO_ROOT, 'docs');
const REPOSITORY_URL = 'https://github.com/ViacheslavChernyshov/java-interview-questions-and-answers';

const SECTION_ICONS = {
  1: '🗄️',
  2: '🧩',
  3: '🧠',
  4: '📦',
  5: '🍃',
  6: '🌐',
  7: '⚡',
  8: '🌊',
  9: '🧵',
  10: '🔑',
  11: '💳',
  12: '🔤',
  13: '🔒',
  14: '🐳',
  15: '📨',
  16: '💾',
  17: '🏗️',
  18: '📐',
  19: '⏱️',
  20: '📋',
};

const LANGUAGES = {
  eng: {
    lang_code: 'en',
    site_prefix: '',
    output_dir: path.join(DOCS_DIR, 'questions'),
    source_dir: path.join(REPO_ROOT, 'eng'),
    label: 'English',
    flag: '🇬🇧',
    library_title: 'Java Interview Questions and Answers Library',
    library_description: 'Browse 500+ Java interview answers directly on the site across Spring Boot, SQL, Hibernate, Kafka, Concurrency, and other backend topics.',
    home_url: '/',
    search_file: 'search-index-en.json',
  },
  ru: {
    lang_code: 'ru',
    site_prefix: 'ru',
    output_dir: path.join(DOCS_DIR, 'ru', 'questions'),
    source_dir: path.join(REPO_ROOT, 'ru'),
    label: 'Русский',
    flag: '🇷🇺',
    library_title: 'Java Interview Questions и ответы на сайте',
    library_description: 'Полная библиотека из 500+ ответов по Java interview: Spring Boot, SQL, Hibernate, Kafka, многопоточность, Docker, Kubernetes и архитектура.',
    home_url: '/ru/',
    search_file: 'search-index-ru.json',
  },
  ua: {
    lang_code: 'uk',
    site_prefix: 'uk',
    output_dir: path.join(DOCS_DIR, 'uk', 'questions'),
    source_dir: path.join(REPO_ROOT, 'ua'),
    label: 'Українська',
    flag: '🇺🇦',
    library_title: 'Java Interview Questions та відповіді на сайті',
    library_description: 'Повна бібліотека відповідей для Java interview: Spring Boot, SQL, Hibernate, Kafka, багатопоточність, Docker, Kubernetes та архітектура.',
    home_url: '/uk/',
    search_file: 'search-index-uk.json',
  },
};

const LOCALIZED_TEXT = {
  eng: {
    library_intro: 'Browse the full answer library directly on the site in English. Every section and question page is generated from the source Markdown files in the repository, so the site and GitHub content stay in sync.',
    library_use_heading: 'How to use this library',
    library_steps: [
      'Pick one topic cluster that matches the role you are targeting.',
      'Open the section page to see the full question sequence.',
      'Read the answer page directly on the site, then switch languages or jump to the next question.',
    ],
    library_sections_heading: 'All sections',
    table_topic: 'Topic',
    table_questions: 'Questions',
    section_questions_heading: 'Questions in this section',
    section_navigator_heading: 'Study navigator',
    section_description: '{count} interview questions and answers in the {label} section.',
    badge_junior: 'Junior',
    badge_middle: 'Middle',
    badge_senior: 'Senior',
  },
  ru: {
    library_intro: 'Открывайте полную библиотеку ответов прямо на сайте на русском языке. Каждая секция и каждая страница вопроса генерируются из исходных Markdown-файлов репозитория.',
    library_use_heading: 'Как пользоваться этой библиотекой',
    library_steps: [
      'Выберите тематический блок под роль, на которую готовитесь.',
      'Откройте страницу секции, чтобы пройти все вопросы по порядку.',
      'Читайте ответ прямо на сайте, переключайте язык или переходите к следующему вопросу.',
    ],
    library_sections_heading: 'Все разделы',
    table_topic: 'Тема',
    table_questions: 'Вопросы',
    section_questions_heading: 'Вопросы этого раздела',
    section_navigator_heading: 'Навигатор по разделу',
    section_description: '{count} вопросов и ответов в разделе {label}.',
    badge_junior: 'Junior',
    badge_middle: 'Middle',
    badge_senior: 'Senior',
  },
  ua: {
    library_intro: 'Відкривайте повну бібліотеку відповідей прямо на сайті українською. Кожна секція і кожна сторінка питання генеруються з вихідних Markdown-файлів репозиторію.',
    library_use_heading: 'Як користуватися цією бібліотекою',
    library_steps: [
      'Оберіть тематичний блок під роль, до якої готуєтесь.',
      'Відкрийте сторінку секції, щоб пройти всі питання по порядку.',
      'Читайте відповідь прямо на сайті, перемикайте мову або переходьте до наступного питання.',
    ],
    library_sections_heading: 'Усі розділи',
    table_topic: 'Тема',
    table_questions: 'Питання',
    section_questions_heading: 'Питання цього розділу',
    section_navigator_heading: 'Навігатор по розділу',
    section_description: '{count} питань і відповідей у розділі {label}.',
    badge_junior: 'Junior',
    badge_middle: 'Middle',
    badge_senior: 'Senior',
  },
};

const SECTION_RE = /^(\d+)\.\s+(.+)$/;
const QUESTION_RE = /^(\d+)\.\s+(.+)\.md$/;
const FRONT_MATTER_RE = /^---\s*\n[\s\S]*?\n---\s*\n/;

function slugify(text) {
  const asciiReplacements = {
    '@': ' at ',
    '&': ' and ',
    '+': ' plus ',
    '/': ' ',
    '_': ' ',
    "'": '',
  };
  let normalized = text.toLowerCase();
  for (const [src, tgt] of Object.entries(asciiReplacements)) {
    normalized = normalized.split(src).join(tgt);
  }
  normalized = normalized.replace(/[^a-z0-9]+/g, '-');
  normalized = normalized.replace(/-{2,}/g, '-').replace(/^-|-$/g, '');
  return normalized || 'item';
}

function yamlQuote(value) {
  if (value === null || value === undefined) return '""';
  const escaped = String(value).replace(/\\/g, '\\\\').replace(/"/g, '\\"');
  return `"${escaped}"`;
}

function renderFrontMatter(data) {
  const lines = ['---'];
  for (const [key, value] of Object.entries(data)) {
    if (Array.isArray(value)) {
      lines.push(`${key}:`);
      for (const item of value) {
        if (typeof item === 'object' && item !== null) {
          lines.push('  -');
          for (const [k, v] of Object.entries(item)) {
            if (Array.isArray(v)) {
              lines.push(`    ${k}:`);
              for (const sub of v) {
                if (typeof sub === 'object') {
                  lines.push('      -');
                  for (const [sk, sv] of Object.entries(sub)) {
                    if (typeof sv === 'number' || typeof sv === 'boolean') {
                      lines.push(`        ${sk}: ${sv}`);
                    } else {
                      lines.push(`        ${sk}: ${yamlQuote(sv)}`);
                    }
                  }
                } else {
                  lines.push(`      - ${yamlQuote(sub)}`);
                }
              }
            } else if (typeof v === 'number' || typeof v === 'boolean') {
              lines.push(`    ${k}: ${v}`);
            } else {
              lines.push(`    ${k}: ${yamlQuote(v)}`);
            }
          }
        } else {
          lines.push(`  - ${yamlQuote(item)}`);
        }
      }
    } else if (typeof value === 'number' || typeof value === 'boolean') {
      lines.push(`${key}: ${value}`);
    } else {
      lines.push(`${key}: ${yamlQuote(value)}`);
    }
  }
  lines.push('---');
  return lines.join('\n');
}

function splitHeading(markdown, fallbackTitle) {
  const text = markdown.replace(FRONT_MATTER_RE, '');
  const lines = text.split('\n');
  if (lines.length > 0 && lines[0].startsWith('# ')) {
    const title = lines[0].substring(2).trim();
    const body = lines.slice(1).join('\n').replace(/^\n+/, '');
    return { title, body };
  }
  return { title: fallbackTitle, body: text.trim() };
}

function extractSummary(body) {
  const paragraphs = [];
  let insideCode = false;
  for (const rawLine of body.split('\n')) {
    const line = rawLine.trim();
    if (line.startsWith('```')) {
      insideCode = !insideCode;
      continue;
    }
    if (insideCode || !line) {
      if (paragraphs.length > 0) break;
      continue;
    }
    if (/^(#|-|\*|\||>|\d+\.)/.test(line)) continue;
    paragraphs.push(line);
  }
  let summary = paragraphs.length ? paragraphs.join(' ') : 'Structured Java interview answer with Junior, Middle, and Senior level explanations.';
  summary = summary.replace(/`([^`]*)`/g, '$1');
  summary = summary.replace(/\[(.*?)\]\((.*?)\)/g, '$1');
  summary = summary.replace(/(\*\*|__|\*|_)/g, '');
  summary = summary.replace(/\s+/g, ' ').trim();
  return summary.length <= 180 ? summary : summary.slice(0, 177).trim() + '...';
}

function siteUrl(langKey, ...parts) {
  const prefix = LANGUAGES[langKey].site_prefix;
  const cleanParts = parts.filter(Boolean).map(p => p.replace(/^\/+|\/+$/g, ''));
  if (prefix) {
    return '/' + [prefix, ...cleanParts].join('/') + '/';
  }
  return cleanParts.length ? '/' + cleanParts.join('/') + '/' : '/';
}

function rewriteNavigatorLinks(navigatorBody, section) {
  let rewritten = navigatorBody;
  for (const question of section.questions) {
    const replacement = `./${question.slug}/`;
    const candidates = [
      question.file_name,
      encodeURIComponent(question.file_name),
      question.file_name.replace(/ /g, '%20'),
    ];
    for (const c of candidates) {
      rewritten = rewritten.split(`](${c})`).join(`](${replacement})`);
    }
  }
  return rewritten;
}

function parseLanguage(langKey) {
  const sourceDir = LANGUAGES[langKey].source_dir;
  const sections = {};

  const entries = fs.readdirSync(sourceDir).sort();
  for (const entryName of entries) {
    const entryPath = path.join(sourceDir, entryName);
    if (!fs.statSync(entryPath).isDirectory() || entryName.startsWith('.')) continue;

    const match = entryName.match(SECTION_RE);
    if (!match) continue;
    const number = parseInt(match[1], 10);
    const label = match[2];

    const files = fs.readdirSync(entryPath).sort();
    const navFile = files.find(f => f.startsWith('00.'));
    if (!navFile) throw new Error(`Navigator file not found in ${entryPath}`);

    const navRaw = fs.readFileSync(path.join(entryPath, navFile), 'utf-8');
    const { title: navTitle, body: navBody } = splitHeading(navRaw, label);

    const questions = [];
    for (const f of files) {
      if (f.startsWith('00.') || f.startsWith('_') || !f.endsWith('.md')) continue;
      const qMatch = f.match(QUESTION_RE);
      if (!qMatch) continue;
      const qNum = parseInt(qMatch[1], 10);
      const qFallback = qMatch[2];
      const qPath = path.join(entryPath, f);
      const raw = fs.readFileSync(qPath, 'utf-8');
      const { title, body } = splitHeading(raw, qFallback);
      const relPath = path.relative(REPO_ROOT, qPath).replace(/\\/g, '/');

      questions.push({
        number: qNum,
        title,
        file_name: f,
        source_path: qPath,
        source_relative_path: relPath,
        body: body.trim(),
        summary: extractSummary(body),
        position: 0,
        slug: '',
        url: '',
        prev_title: '',
        prev_url: '',
        next_title: '',
        next_url: '',
      });
    }

    questions.sort((a, b) => a.number - b.number);
    questions.forEach((q, idx) => { q.position = idx + 1; });

    sections[number] = {
      number,
      label,
      dir_name: entryName,
      source_dir: entryPath,
      navigator_path: path.join(entryPath, navFile),
      navigator_body: navBody.trim(),
      navigator_title: navTitle,
      icon: SECTION_ICONS[number] || '📚',
      slug: '',
      url: '',
      questions,
    };
  }

  return sections;
}

function assignSharedSlugs(allSections) {
  const engSections = allSections.eng;
  for (const sNum of Object.keys(engSections).map(Number).sort((a, b) => a - b)) {
    const sec = engSections[sNum];
    sec.slug = `${String(sec.number).padStart(2, '0')}-${slugify(sec.label)}`;
    sec.url = siteUrl('eng', 'questions', sec.slug);
    for (const q of sec.questions) {
      q.slug = `${String(q.position).padStart(2, '0')}-${slugify(q.title)}`;
      q.url = siteUrl('eng', 'questions', sec.slug, q.slug);
    }
  }

  for (const [langKey, sections] of Object.entries(allSections)) {
    if (langKey === 'eng') continue;
    for (const sNum of Object.keys(sections).map(Number).sort((a, b) => a - b)) {
      const sec = sections[sNum];
      const engSec = engSections[sNum];
      sec.slug = engSec.slug;
      sec.url = siteUrl(langKey, 'questions', sec.slug);
      for (let i = 0; i < sec.questions.length; i++) {
        const q = sec.questions[i];
        if (i < engSec.questions.length) {
          const eq = engSec.questions[i];
          q.position = eq.position;
          q.slug = eq.slug;
        } else {
          q.position = i + 1;
          q.slug = `${String(q.position).padStart(2, '0')}-${slugify(q.title)}`;
        }
        q.url = siteUrl(langKey, 'questions', sec.slug, q.slug);
      }
    }
  }
}

function assignPrevNext(section) {
  for (let i = 0; i < section.questions.length; i++) {
    const q = section.questions[i];
    if (i > 0) {
      const pq = section.questions[i - 1];
      q.prev_title = pq.title;
      q.prev_url = pq.url;
    }
    if (i + 1 < section.questions.length) {
      const nq = section.questions[i + 1];
      q.next_title = nq.title;
      q.next_url = nq.url;
    }
  }
}

function buildAlternates(allSections, sectionNumber, questionPosition = null) {
  const alternates = [];
  let defaultUrl = allSections.eng[sectionNumber].url;

  for (const [langKey, langConfig] of Object.entries(LANGUAGES)) {
    const sec = allSections[langKey][sectionNumber];
    let url = sec.url;
    if (questionPosition !== null) {
      const qMap = new Map(sec.questions.map(q => [q.position, q]));
      if (!qMap.has(questionPosition)) continue;
      url = qMap.get(questionPosition).url;
      if (langKey === 'eng') defaultUrl = url;
    } else if (langKey === 'eng') {
      defaultUrl = url;
    }
    alternates.push({ lang: langConfig.lang_code, label: langConfig.label, flag: langConfig.flag, url });
  }
  alternates.push({ lang: 'x-default', label: 'Default', flag: '🌐', url: defaultUrl });
  return alternates;
}

function buildSidebarData(sections, currentSectionNumber = null, currentQuestionPosition = null) {
  return sections.map(s => ({
    number: s.number,
    label: s.label,
    icon: s.icon,
    slug: s.slug,
    url: s.url,
    count: s.questions.length,
    is_current: s.number === currentSectionNumber,
    questions: s.questions.map(q => ({
      position: q.position,
      title: q.title,
      slug: q.slug,
      url: q.url,
      is_current: s.number === currentSectionNumber && q.position === currentQuestionPosition,
    })),
  }));
}

function buildLibraryContent(langKey, sections) {
  const lang = LANGUAGES[langKey];
  const text = LOCALIZED_TEXT[langKey];
  const lines = [
    `# ${lang.library_title}`,
    '',
    text.library_intro,
    '',
    `## ${text.library_use_heading}`,
    '',
  ];
  for (const step of text.library_steps) {
    lines.push(`- ${step}`);
  }
  lines.push('', `## ${text.library_sections_heading}`, '');
  lines.push(`| # | | ${text.table_topic} | ${text.table_questions} |`);
  lines.push('| --- |:---:| --- |:---:|');
  for (const s of sections) {
    lines.push(`| ${s.number} | ${s.icon} | [${s.label}](./${s.slug}/) | ${s.questions.length} |`);
  }
  return lines.join('\n') + '\n';
}

function buildSectionContent(langKey, section) {
  const text = LOCALIZED_TEXT[langKey];
  const rewrittenNav = rewriteNavigatorLinks(section.navigator_body, section);
  const lines = [
    `## ${text.section_questions_heading}`,
    '',
  ];
  for (const q of section.questions) {
    lines.push(`${q.position}. [${q.title}](./${q.slug}/)`);
  }
  lines.push('', `## ${text.section_navigator_heading}`, '', rewrittenNav, '');
  return lines.join('\n');
}

function buildQuestionContent(question) {
  return question.body.trim() + '\n';
}

function ensureCleanOutput() {
  for (const config of Object.values(LANGUAGES)) {
    if (fs.existsSync(config.output_dir)) {
      fs.rmSync(config.output_dir, { recursive: true, force: true });
    }
    fs.mkdirSync(config.output_dir, { recursive: true });
  }
}

function writePage(filePath, frontMatter, content) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  const full = renderFrontMatter(frontMatter) + '\n\n' + content.trim() + '\n';
  fs.writeFileSync(filePath, full, 'utf-8');
}

function generateSearchIndexes(allSections) {
  const dataDir = path.join(DOCS_DIR, 'assets', 'data');
  if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });

  for (const [langKey, langConfig] of Object.entries(LANGUAGES)) {
    const items = [];
    const sections = allSections[langKey];
    for (const sec of Object.values(sections)) {
      for (const q of sec.questions) {
        items.push({
          id: `${sec.number}-${q.position}`,
          title: q.title,
          secNumber: sec.number,
          secTitle: sec.label,
          icon: sec.icon,
          pos: q.position,
          url: q.url,
          summary: q.summary,
        });
      }
    }
    const target = path.join(dataDir, langConfig.search_file);
    fs.writeFileSync(target, JSON.stringify(items), 'utf-8');
    console.log(`Generated search index: ${target} (${items.length} items)`);
  }
}

function generatePages(allSections) {
  ensureCleanOutput();

  for (const [langKey, langConfig] of Object.entries(LANGUAGES)) {
    const sections = allSections[langKey];
    const orderedSections = Object.keys(sections).map(Number).sort((a, b) => a - b).map(n => sections[n]);

    for (const sec of orderedSections) {
      assignPrevNext(sec);
    }

    const outputDir = langConfig.output_dir;
    const allSectionsMeta = buildSidebarData(orderedSections);

    // 1. Library index page
    writePage(
      path.join(outputDir, 'index.md'),
      {
        layout: 'content-page',
        kind: 'library',
        title: langConfig.library_title,
        description: langConfig.library_description,
        lang: langConfig.lang_code,
        language_label: langConfig.label,
        language_flag: langConfig.flag,
        home_url: langConfig.home_url,
        library_url: siteUrl(langKey, 'questions'),
        alternates: Object.values(LANGUAGES).map(l => ({
          lang: l.lang_code,
          label: l.label,
          flag: l.flag,
          url: siteUrl(Object.keys(LANGUAGES).find(k => LANGUAGES[k] === l), 'questions'),
        })).concat([{ lang: 'x-default', label: 'Default', flag: '🌐', url: siteUrl('eng', 'questions') }]),
        sidebar_sections: allSectionsMeta,
      },
      buildLibraryContent(langKey, orderedSections)
    );

    // 2. Section pages & Question pages
    for (const sec of orderedSections) {
      const secSidebar = buildSidebarData(orderedSections, sec.number);
      const secRelative = path.relative(REPO_ROOT, sec.navigator_path).replace(/\\/g, '/');

      writePage(
        path.join(outputDir, sec.slug, 'index.md'),
        {
          layout: 'content-page',
          kind: 'section',
          title: sec.label,
          icon: sec.icon,
          description: LOCALIZED_TEXT[langKey].section_description.replace('{count}', sec.questions.length).replace('{label}', sec.label),
          lang: langConfig.lang_code,
          language_label: langConfig.label,
          language_flag: langConfig.flag,
          home_url: langConfig.home_url,
          library_url: siteUrl(langKey, 'questions'),
          section_title: sec.label,
          section_url: sec.url,
          section_number: sec.number,
          question_count: sec.questions.length,
          source_url: `${REPOSITORY_URL}/blob/master/${secRelative}`,
          alternates: buildAlternates(allSections, sec.number),
          sidebar_sections: secSidebar,
        },
        buildSectionContent(langKey, sec)
      );

      for (const q of sec.questions) {
        const qSidebar = buildSidebarData(orderedSections, sec.number, q.position);
        writePage(
          path.join(outputDir, sec.slug, q.slug, 'index.md'),
          {
            layout: 'content-page',
            kind: 'question',
            title: q.title,
            icon: sec.icon,
            description: q.summary,
            lang: langConfig.lang_code,
            language_label: langConfig.label,
            language_flag: langConfig.flag,
            home_url: langConfig.home_url,
            library_url: siteUrl(langKey, 'questions'),
            section_title: sec.label,
            section_url: sec.url,
            section_number: sec.number,
            question_number: q.position,
            source_url: `${REPOSITORY_URL}/blob/master/${q.source_relative_path}`,
            prev_title: q.prev_title,
            prev_url: q.prev_url,
            next_title: q.next_title,
            next_url: q.next_url,
            alternates: buildAlternates(allSections, sec.number, q.position),
            sidebar_sections: qSidebar,
          },
          buildQuestionContent(q)
        );
      }
    }
  }

  generateSearchIndexes(allSections);
}

function main() {
  console.log('Parsing all language directories...');
  const allSections = {
    eng: parseLanguage('eng'),
    ru: parseLanguage('ru'),
    ua: parseLanguage('ua'),
  };

  assignSharedSlugs(allSections);
  generatePages(allSections);

  const totalQuestions = Object.values(allSections.eng).reduce((acc, s) => acc + s.questions.length, 0);
  console.log(`✅ Successfully generated ${totalQuestions} question pages per language across 20 sections!`);
}

main();
