# Deep Learning Curriculum and Ontology Mapping

Status: proposed knowledge integration; not runtime deployment
Source: Simon J. D. Prince, *Understanding Deep Learning*, https://udlbook.github.io/udlbook/
Recorded: 2026-10-20

## Curriculum sequence
1. Introduction
2. Supervised learning
3. Shallow neural networks
4. Deep neural networks
5. Loss functions
6. Fitting models
7. Gradients and initialization
8. Convolutional networks
9. Transformers
10. Free PDF, notebooks, exercises, and supporting materials

## Ontology nodes
- LearningResource: Understanding Deep Learning (source URL, author, format, provenance)
- LearningModule: ten curriculum entries, ordered and linked to the resource
- MLConcept: supervised learning, neural network, loss, fitting, gradient, initialization, convolution, attention, transformer, generative model
- EngineeringCapability: model training, inference, evaluation, optimization, representation learning
- EvidenceArtifact: dataset provenance, evaluation result, reproducibility record, model card, experiment receipt
- GovernanceConstraint: training authorization, dataset rights, privacy, model risk, deployment approval

## Typed relationships
- LearningResource HAS_MODULE LearningModule
- LearningModule TEACHES MLConcept
- MLConcept INFORMS EngineeringCapability
- EngineeringCapability REQUIRES_EVIDENCE EvidenceArtifact
- EngineeringCapability SUBJECT_TO GovernanceConstraint
- EngineeringCapability MAY_SUPPORT ProjectComponent

## Proposed component mappings (not claims of deployed integrations)
- ATG: transformer and structured-language representation concepts
- NemoClaw/Nemotron runtime: inference and model architecture literacy
- FIN54: prediction, fitting, leakage prevention, uncertainty, backtesting
- VERITY: reproducible evaluations and evidence verification
- AEGIS: model risk, permission boundaries, approval requirements

## Learning gates
- Foundations: articulate supervised learning and distinguish training/inference
- Optimization: implement loss, gradients, fitting and validation on toy data
- Architectures: compare CNNs and transformers with documented limitations
- Systems: produce an independently reviewable evaluation and model card
- Promotion: human approval, bounded execution envelope, signed receipt and audit

## Assurance
- Curriculum inclusion is not evidence of agent learning or model competence.
- Source materials must be checked for licensing before redistribution; link rather than copy.
- Salary claims in circulating graphics are unverified and excluded from ontology facts.
- No production permissions, financial trading authority, training jobs, or deployment are granted.
- All runtime changes require separate implementation, tests, VERITY review, and existing branch protection.
