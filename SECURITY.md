# Security policy

EvidenceLens is in the design phase and has no supported production release yet. Before a deployable release, the project must publish supported versions, reporting arrangements, and tested security controls.

For sensitive findings, use GitHub's private vulnerability reporting if it is enabled on this repository. If that option is unavailable, contact the maintainer through a verified private channel listed on their GitHub profile and request a reporting route. Do not disclose credentials, patient information, exploit details, or private source content in a public issue. General non-sensitive design concerns can be discussed publicly.

Relevant risks include source and retrieval poisoning, prompt injection, unsupported medical claims, unsafe output rendering, URL-ingestion SSRF, parser abuse, authorization bypass, cross-user cache/retrieval exposure, secrets leakage, and uncontrolled model consumption.

Implementation must map applicable OWASP ASVS and LLM controls to observable verification. Maintain threat models for ingestion, retrieval, generation, and publishing boundaries. Automated checks supplement manual review; the repository does not claim certification or complete protection against these risks.
