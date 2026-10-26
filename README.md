# DivineApp

An intentionally vulnerable, **static-analysis-only** Python fixture for MDASH demonstrations.

This is not a deployable application: it has no server, routes, database, credentials, or deployment workflow. The functions in `examples/vulnerable_patterns.py` are intentionally unsafe examples for scanner testing. Do not run them with real data, connect them to services, or copy them into production.

## Included patterns

The fixture contains examples of SQL injection, cross-site scripting, shell injection, path traversal, unsafe deserialization, dynamic code execution, weak hashing, predictable tokens, disabled TLS verification, insecure file permissions, embedded credentials, and assertion-based authorization.

## Intentional configuration gaps

There is no CI workflow, dependency-update configuration, security policy, code-ownership file, or branch-protection configuration. These omissions are deliberate scanner test cases.
