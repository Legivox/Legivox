"""Shared identifiers for source-grounded single-post plans."""

RSS_GROQ_PLAN_SOURCE = "RSS feeds + Groq editorial ranking"
MULTIDOMAIN_PLAN_SOURCE = "Multidomain discovery + independent editorial review"
SOURCE_GROUNDED_SINGLE_POST_SOURCES = frozenset({
    RSS_GROQ_PLAN_SOURCE,
    MULTIDOMAIN_PLAN_SOURCE,
})
