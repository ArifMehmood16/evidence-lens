# Feature specification template

Use for a substantial behavior change; small fixes can cover these points in the PR. Replace the prompts with concrete decisions before implementation.

## User problem and scope

Who needs this behavior, what outcome is useful, and what is outside this change?

## Observable acceptance criteria

Describe the success, failure, and boundary cases in verifiable terms. Define measurable budgets only where needed.

## Contracts and reuse

Describe input/output and evidence contracts. Identify existing components or maintained libraries to reuse and any justified dependency changes.

## Security and data handling

Identify trust boundaries, authorization, source permissions, untrusted inputs, and applicable OWASP controls with verification methods.

## Evaluation and operations

Identify meaningful tests, RAG evaluation slices, telemetry, costs, and degraded behavior. For changes to state or indexes, describe migration and rollback.

## Delivery

Describe the smallest complete implementation slice and any unresolved decision that actually blocks it.
