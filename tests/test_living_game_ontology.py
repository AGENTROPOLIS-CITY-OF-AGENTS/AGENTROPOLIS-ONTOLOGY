#!/usr/bin/env python3
"""Living Game ontology conformance. Run: python3 -m unittest tests/test_living_game_ontology.py"""

import json
import os
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CLASSES = yaml.safe_load((ROOT / "ontology/living-game-classes.yaml").read_text())
INVARIANTS = yaml.safe_load((ROOT / "governance/living-game-invariants.yaml").read_text())
ENTITIES = CLASSES["entities"]

LGO_ID = "https://agentropolis.dev/schemas/living-game-object-v1.schema.json"
LRS_ID = "https://agentropolis.dev/schemas/live-reality-session-v1.schema.json"
ENVELOPE_ID = "https://agentropolis.dev/atg/contracts/core/execution-envelope.schema.json"


class LivingGameOntologyTest(unittest.TestCase):
    def test_references_canonical_schemas(self):
        self.assertEqual(CLASSES["canonical_sources"]["schemas"]["living_game_object"], LGO_ID)
        self.assertEqual(CLASSES["canonical_sources"]["schemas"]["live_reality_session"], LRS_ID)
        self.assertEqual(ENTITIES["LivingGameObject"]["schema"], LGO_ID)
        self.assertEqual(ENTITIES["LiveRealitySession"]["schema"], LRS_ID)

    def test_does_not_define_an_execution_envelope(self):
        env = ENTITIES["ExecutionEnvelope"]
        self.assertEqual(env["authority_owner"], "atg")
        self.assertEqual(env["schema"], ENVELOPE_ID)
        self.assertFalse(env["defined_in_this_ontology"])
        for key in ("required_fields", "fields", "properties"):
            self.assertNotIn(key, env)
        self.assertEqual(CLASSES["canonical_sources"]["execution_envelope"]["owner"], "AGENTROPOLIS-ATG")

    def test_required_classes_registered(self):
        for name in (
            "LivingGameObject", "HumanSignalEntity", "DeviceCapability", "PhysicalAuthenticator",
            "QuestTrigger", "LiveRealitySession", "BroadcastDestination", "InteroperabilityAdapter",
        ):
            self.assertIn(name, ENTITIES)
            self.assertIn("authority_owner", ENTITIES[name])
            self.assertIn("epistemic_type", ENTITIES[name])

    def test_evidence_like_classes_never_grant_authority(self):
        self.assertFalse(ENTITIES["Evidence"]["grants_authority"])
        self.assertFalse(ENTITIES["PhysicalAuthenticator"]["grants_authority"])
        self.assertFalse(ENTITIES["PhysicalAuthenticator"]["may_transfer_value_or_ownership"])
        self.assertFalse(ENTITIES["QuestTrigger"]["grants_authority"])
        self.assertFalse(ENTITIES["DeviceCapability"]["connectivity_grants_authority"])
        self.assertFalse(ENTITIES["HumanSignalEntity"]["popularity_grants_authority"])
        self.assertFalse(ENTITIES["SignalMagnet"]["reach_grants_authority"])

    def test_privacy_and_broadcast_defaults(self):
        session = ENTITIES["LiveRealitySession"]
        self.assertEqual(session["privacy_defaults"], {
            "rawFrameRetention": "ephemeral",
            "locationMode": "hidden",
            "faceRecognition": False,
            "publicBroadcastAuthorized": False,
        })
        self.assertFalse(session["face_recognition_permitted"])
        self.assertIn("ExecutionEnvelope", session["public_egress_requires"])
        self.assertFalse(ENTITIES["BroadcastDestination"]["raw_credentials_permitted"])
        self.assertFalse(ENTITIES["BroadcastLease"]["unbounded_duration_permitted"])

    def test_interoperability_is_explicit_and_non_authoritative(self):
        adapter = ENTITIES["InteroperabilityAdapter"]
        self.assertFalse(adapter["implicit_interoperability_permitted"])
        self.assertFalse(adapter["output_is_authoritative"])
        self.assertEqual(adapter["fields"], ["targetSystem", "balancePolicy", "permittedTraits", "prohibitedEffects"])

    def test_accessibility_alternatives_required_for_physical_triggers(self):
        trig = ENTITIES["QuestTrigger"]
        for t in ("nfc", "qr", "location", "gesture", "ar_anchor", "vr_location", "wallet_proof"):
            self.assertIn(t, trig["requires_accessibility_alternative_for"])
            self.assertIn(t, trig["types"])

    def test_invariants_cover_hard_rules(self):
        ids = {i["id"] for i in INVARIANTS["invariants"]}
        for required in (
            "observation-is-evidence", "consequential-requires-envelope", "single-execution-envelope",
            "no-tap-to-spend", "no-face-recognition", "no-silent-public-broadcast",
            "accessibility-alternatives", "game-authority", "brand-neutral-devices",
        ):
            self.assertIn(required, ids)
        critical = {i["id"] for i in INVARIANTS["invariants"] if i["severity"] == "critical"}
        self.assertIn("single-execution-envelope", critical)
        self.assertIn("no-face-recognition", critical)

    def test_franchise_neutral(self):
        text = (ROOT / "ontology/living-game-classes.yaml").read_text().lower()
        text += (ROOT / "docs/LIVING_GAME_ONTOLOGY.md").read_text().lower()
        for banned in ("doginal", "ddhq", "openclaw is permitted"):
            self.assertNotIn(banned, text)

    def test_enums_match_gaming_district(self):
        schema_dir = os.environ.get("LIVING_GAME_SCHEMA_DIR")
        if not schema_dir:
            self.skipTest("LIVING_GAME_SCHEMA_DIR not set")
        lgo = json.loads((Path(schema_dir) / "schemas/living-game-object-v1.schema.json").read_text())
        lrs = json.loads((Path(schema_dir) / "schemas/live-reality-session-v1.schema.json").read_text())
        self.assertEqual(lgo["$id"], LGO_ID)
        self.assertEqual(lrs["$id"], LRS_ID)
        p = lgo["properties"]
        self.assertEqual(ENTITIES["LivingGameObject"]["object_types"], p["objectType"]["enum"])
        self.assertEqual(ENTITIES["PhysicalAuthenticator"]["assurance_tiers"], p["physical"]["properties"]["assuranceTier"]["enum"])
        adapter_fields = list(p["interoperability"]["properties"]["adapters"]["items"]["properties"].keys())
        self.assertEqual(ENTITIES["InteroperabilityAdapter"]["fields"], adapter_fields)
        q = lrs["properties"]
        self.assertEqual(ENTITIES["LiveRealitySession"]["modes"], q["mode"]["enum"])
        self.assertEqual(ENTITIES["LiveRealitySession"]["states"], q["state"]["enum"])
        self.assertEqual(ENTITIES["DeviceCapability"]["values"], q["capabilities"]["items"]["enum"])
        self.assertEqual(ENTITIES["DeviceCapability"]["device_classes"], q["deviceClass"]["enum"])
        self.assertEqual(ENTITIES["BroadcastDestination"]["protocols"], q["destinations"]["items"]["properties"]["protocol"]["enum"])
        self.assertEqual(ENTITIES["BroadcastDestination"]["layouts"], q["destinations"]["items"]["properties"]["layout"]["enum"])
        self.assertEqual(list(ENTITIES["LiveRealitySession"]["privacy_defaults"].keys()), q["privacy"]["required"])


if __name__ == "__main__":
    unittest.main()
