from strictdoc.core.project_config import ProjectConfig


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="DiggerRouter",
        dir_for_sdoc_cache="output/_cache",
        project_features=[
            "TABLE_SCREEN",
            "TRACEABILITY_SCREEN",
            "DEEP_TRACEABILITY_SCREEN",
            "TRACEABILITY_MATRIX_SCREEN",
            "SEARCH",
            "PROJECT_STATISTICS_SCREEN",
            "DIFF",
            # Verknüpft Anforderungen mit dem Quellcode, sobald es welchen gibt.
            "REQUIREMENT_TO_SOURCE_TRACEABILITY",
            # ALL_FEATURES schaltet STATIC_EDITING nicht ein.
            "STATIC_EDITING",
        ],
        grammars={
            "@diggerrouter": "req/sdoc/grammar.sgra",
        },
        include_doc_paths=[
            "/req/sdoc/",
        ],
    )
