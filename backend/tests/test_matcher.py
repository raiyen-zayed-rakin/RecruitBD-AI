from services.matcher.cv_matcher import skill_weight, experience_score, get_degree_level


def test_skill_weight():
    """Test that core, soft, and unknown skills get the correct weights."""
    # Core skills (assuming 'python' and 'react' are in CORE_SKILLS)
    assert skill_weight("python") == 1.5
    assert skill_weight("react") == 1.5

    # Soft skills (assuming 'communication' is in SOFT_SKILLS)
    assert skill_weight("communication") == 0.3

    # Unknown/Standard skills
    assert skill_weight("obscure_framework_123") == 1.0


def test_experience_score():
    """Test the experience penalty/bonus logic."""
    # If job requires 0 years, anyone passes
    assert experience_score(cv_years=2, required_years=0) == 1.0

    # If CV years >= required years, full points
    assert experience_score(cv_years=5, required_years=5) == 1.0
    assert experience_score(cv_years=7, required_years=5) == 1.0

    # Partial matches (based on your custom logic)
    assert experience_score(cv_years=4, required_years=5) == 0.75  # 80% coverage (>= 70%)
    assert experience_score(cv_years=2, required_years=5) == 0.40  # 40% coverage (>= 40%)
    assert experience_score(cv_years=1, required_years=5) == 0.10  # 20% coverage (< 40%)


def test_get_degree_level():
    """Test that education text is properly converted to level integers."""
    assert get_degree_level("B.Sc in Computer Science") == 4
    assert get_degree_level("MSc in Data Science") == 5
    assert get_degree_level("HSC") == 2
    assert get_degree_level("Secondary School Certificate") == 1
    assert get_degree_level("Some unknown text") == 0
