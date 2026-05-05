"""
constants.py — Shared constants for the matcher package
---------------------------------------------------------
Single source of truth for CORE_SKILLS, SENIORITY_MAP, and
SKILL_SYNONYMS used by both build_index.py and cv_matcher.py.
"""

import re

# ── SKILL SYNONYMS ────────────────────────────────────────────────────────────

SKILL_SYNONYMS = [
    {"javascript", "js", "node.js", "nodejs"},
    {"typescript", "ts"},
    {"python", "py"},
    {"java", "core java"},
    {"c++", "cpp"},
    {"c#", "csharp"},
    {"machine learning", "ml"},
    {"deep learning", "dl"},
    {"natural language processing", "nlp"},
    {"computer vision", "cv"},
    {"artificial intelligence", "ai"},
    {"sql", "mysql", "postgresql", "postgres", "oracle sql"},
    {"mongodb", "mongo"},
    {"react", "react.js", "reactjs"},
    {"vue", "vue.js", "vuejs"},
    {"angular", "angularjs"},
    {"flutter", "dart"},
    {"spring boot", "spring"},
    {"git", "github", "gitlab"},
    {"docker", "containerization"},
    {"kubernetes", "k8s"},
    {"aws", "amazon web services"},
    {"gcp", "google cloud"},
    {"azure", "microsoft azure"},
    {"rest", "rest api", "restful"},
    {"graphql", "gql"},
    {"ci cd", "cicd", "continuous integration", "continuous delivery"},
    {"microservices", "microservice architecture"},
    {"oop", "object oriented programming"},
    {"dsa", "data structures and algorithms"},
    {"unit testing", "test automation", "automated testing"},
    {"pytest", "py test"},
    {"pandas", "python pandas"},
    {"numpy", "python numpy"},
    {"power bi", "powerbi", "bi dashboard"},
    {"tableau", "tableau bi"},
    {"excel", "ms excel", "microsoft excel"},
    {"firebase", "firestore"},
    {"adobe premiere pro", "premiere pro", "premiere"},
    {"adobe photoshop", "photoshop", "ps"},
    {"adobe illustrator", "illustrator", "ai design"},
    {"after effects", "adobe after effects"},
    {"figma", "ui ux", "ux ui", "user interface", "user experience"},
    {"seo", "search engine optimization"},
    {"sem", "search engine marketing"},
    {"digital marketing", "social media marketing", "smm"},
    {"content writing", "copywriting"},
    {"sales", "business development", "bd"},
    {"customer support", "customer service"},
    {"crm", "customer relationship management"},
    {"accounting", "bookkeeping", "accounts"},
    {"recruitment", "talent acquisition", "hr"},
    {"project management", "agile", "scrum"},
    {"manual testing", "qa", "quality assurance"},
    {"electrical", "electrical maintenance"},
    {"autocad", "cad"},
    {"nursing", "patient care"},
    {"teaching", "tutoring", "home tutor"},
    {"video editing", "video editor"},
    {"graphic design", "graphics design"},
    {"wordpress", "wp"},
    {"shopify", "shopify development"},
    {"laravel", "php laravel"},
    {"react native", "rn"},
    {"kotlin", "android kotlin"},
    {"swift", "ios swift"},
    {"redis", "redis cache"},
    {"elasticsearch", "elastic search"},
    {"fastapi", "python fastapi"},
    {"flask", "python flask"},
    {"django", "python django"},
    {"next.js", "nextjs"},
    {"express", "express.js", "expressjs"},
    {"html", "html5"},
    {"css", "css3", "scss"},
    {"linux", "ubuntu", "unix"},
]

CORE_SKILLS = {
    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "c#",
    "sql",
    "dart",
    "flutter",
    "react",
    "node.js",
    "spring boot",
    "graphql",
    "microservices",
    "ci cd",
    "unit testing",
    "pytest",
    "django",
    "fastapi",
    "flask",
    "machine learning",
    "deep learning",
    "nlp",
    "computer vision",
    "ai",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "mongodb",
    "postgresql",
    "git",
    "rest api",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "power bi",
    "tableau",
    "go",
    "kotlin",
    "swift",
    "php",
    "ruby",
    "scala",
    "redis",
    "firebase",
    "firestore",
    "android",
    "ios",
    "jetpack compose",
    "selenium",
    "jenkins",
    "linux",
    "bash",
    "r",
    "matlab",
    "vue",
    "angular",
    "express",
    "next.js",
    "react native",
    "wordpress",
    "shopify",
    "laravel",
    "postgres",
    "mysql",
    "json",
    "protobuf",
    "oop",
    "dsa",
    "excel",
    "project management",
    "agile",
    "scrum",
    "manual testing",
    "qa",
    "seo",
    "sem",
    "digital marketing",
    "smm",
    "content writing",
    "copywriting",
    "sales",
    "business development",
    "customer support",
    "customer service",
    "crm",
    "accounting",
    "bookkeeping",
    "recruitment",
    "hr",
    "graphic design",
    "video editing",
    "adobe photoshop",
    "adobe illustrator",
    "adobe premiere pro",
    "after effects",
    "figma",
    "ui ux",
    "autocad",
    "electrical",
    "nursing",
    "patient care",
    "teaching",
    "tutoring",
}

SOFT_SKILLS = {
    "leadership",
    "communication",
    "teamwork",
    "collaboration",
    "time management",
    "critical thinking",
    "active listening",
    "problem solving",
    "adaptability",
    "presentation",
}

SENIORITY_MAP = {
    "intern": 0,
    "trainee": 0,
    "fresher": 0,
    "junior": 1,
    "jr": 1,
    "associate": 2,
    "executive": 2,
    "officer": 2,
    "senior": 3,
    "sr": 3,
    "lead": 4,
    "manager": 4,
    "head": 5,
    "director": 5,
    "gm": 5,
}


# ── PRE-COMPILED REGEX PATTERNS ──────────────────────────────────────────────
# Build once at import time — eliminates repeated re.compile() in hot loops.

def _build_word_pattern(term: str) -> re.Pattern:
    """Compile a word-boundary pattern for a skill/keyword."""
    return re.compile(r"\b" + re.escape(term.lower()) + r"\b")


# Patterns for every core skill
CORE_SKILL_PATTERNS: dict[str, re.Pattern] = {
    skill: _build_word_pattern(skill) for skill in CORE_SKILLS
}

# Patterns for every synonym variant
SYNONYM_PATTERNS: dict[str, re.Pattern] = {}
for _group in SKILL_SYNONYMS:
    for _variant in _group:
        if _variant not in SYNONYM_PATTERNS:
            SYNONYM_PATTERNS[_variant] = _build_word_pattern(_variant)

# Patterns for seniority keywords
SENIORITY_PATTERNS: dict[str, re.Pattern] = {
    kw: _build_word_pattern(kw) for kw in SENIORITY_MAP
}


def build_synonym_map() -> dict[str, str]:
    mapping = {}
    for group in SKILL_SYNONYMS:
        canonical = sorted(group)[0]
        for variant in group:
            mapping[variant] = canonical
    return mapping


SYNONYM_MAP = build_synonym_map()
