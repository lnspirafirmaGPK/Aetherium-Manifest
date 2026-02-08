import unittest

from api_gateway.deterministic_replay import replay_lockstep
from tools.benchmarks.creative_stress_scenarios import run_scenarios
from tools.benchmarks.intent_light_knowledge_graph import build_graph
from tools.benchmarks.latency_perception_benchmark import run_benchmark
from tools.contracts.contract_checker import _apply_contract_policy


class DeterministicReplayTests(unittest.TestCase):
    def test_replay_lockstep_with_seed_and_log(self) -> None:
        event_log = [
            {"tick": 1, "event_type": "emotion", "intent": "comfort", "amplitude": 0.3},
            {"tick": 2, "event_type": "intent_switch", "intent": "guide", "amplitude": 0.4},
        ]
        result = replay_lockstep(seed=42, event_log=event_log, node_count=3)
        self.assertTrue(result["lockstep"])
        self.assertEqual(len(set(result["digests"])), 1)


class LatencyPerceptionBenchmarkTests(unittest.TestCase):
    def test_perception_benchmark_separate_from_raw_rtt(self) -> None:
        samples = [
            {"raw_rtt_ms": 50, "render_pipeline_ms": 34, "cognitive_settle_ms": 40, "prediction_mismatch": 0.1},
            {"raw_rtt_ms": 55, "render_pipeline_ms": 36, "cognitive_settle_ms": 43, "prediction_mismatch": 0.0},
        ]
        result = run_benchmark(samples)
        self.assertIn("raw_rtt_ms", result)
        self.assertIn("perceived_latency_ms", result)
        self.assertNotEqual(result["raw_rtt_ms"]["mean"], result["perceived_latency_ms"]["mean"])


class CreativeStressScenarioTests(unittest.TestCase):
    def test_manifestation_gate_stress_cases(self) -> None:
        result = run_scenarios()
        self.assertTrue(result["checks"]["no_spam"])
        self.assertTrue(result["checks"]["no_state_lie"])


class IntentLightKnowledgeGraphTests(unittest.TestCase):
    def test_graph_builder_applies_k_anon(self) -> None:
        records = [
            {"intent": "comfort", "light_pattern": "violet", "operator_confidence": 0.9},
            {"intent": "comfort", "light_pattern": "violet", "operator_confidence": 0.8},
            {"intent": "comfort", "light_pattern": "violet", "operator_confidence": 0.7},
            {"intent": "rare", "light_pattern": "flash", "operator_confidence": 0.95},
        ]
        graph = build_graph(records, min_k_anon=3)
        targets = {(edge["source"], edge["target"]) for edge in graph["edges"]}
        self.assertIn(("comfort", "violet"), targets)
        self.assertNotIn(("rare", "flash"), targets)


class ContractPolicyTests(unittest.TestCase):
    def test_embodiment_injects_deterministic_cadence_default(self) -> None:
        payload = {
            "contract_type": "EMBODIMENT_V1",
            "temporal_state": {"phase": "processing", "stability": 0.7},
            "visual_manifestation": {
                "core_shape": "ring",
                "particle_velocity": 0.3,
                "turbulence": 0.1,
                "chromatic_aberration": 0.02,
            },
        }
        audits: list[str] = []
        errors = _apply_contract_policy("embodiment_v1", payload, audits, mode="legacy")
        self.assertEqual(errors, [])
        self.assertEqual(payload["visual_manifestation"]["cadence"]["bpm"], 110.0)
        self.assertTrue(audits)

    def test_strict_mode_rejects_missing_cadence(self) -> None:
        payload = {
            "contract_type": "EMBODIMENT_V1",
            "input_signal": {"source_model": "x", "latency_ms": 1, "reasoning_depth": 0.1},
            "intent": {"category": "guide", "confidence": 0.8},
            "cognitive_state": {"certainty": 0.7},
            "temporal_state": {"phase": "processing", "stability": 0.7},
            "visual_manifestation": {
                "core_shape": "ring",
                "particle_velocity": 0.3,
                "turbulence": 0.1,
                "chromatic_aberration": 0.02
            }
        }
        schema = {
            "type": "object",
            "required": ["visual_manifestation"],
            "properties": {
                "visual_manifestation": {
                    "type": "object",
                    "required": ["cadence"],
                    "properties": {"cadence": {"type": "object"}}
                }
            }
        }
        audits: list[str] = []
        policy_errors = _apply_contract_policy("embodiment_v1", payload, audits, mode="strict")
        from tools.contracts.contract_checker import _validate

        schema_errors = _validate(schema, payload)
        self.assertEqual(policy_errors, [])
        self.assertTrue(schema_errors)

    def test_ipw_policy_rejects_invalid_probability_sum(self) -> None:
        payload = {
            "ipw_type": "IPW_V1",
            "predictions": [
                {"action_id": "A", "p": 0.9},
                {"action_id": "B", "p": 0.9},
            ],
            "probability_policy": {
                "requires_normalization": True,
                "epsilon": 0.0001,
                "on_violation": "error",
            },
        }
        audits: list[str] = []
        errors = _apply_contract_policy("ipw_v1", payload, audits, mode="strict")
        self.assertTrue(errors)

    def test_ipw_policy_normalizes_when_configured(self) -> None:
        payload = {
            "ipw_type": "IPW_V1",
            "predictions": [
                {"action_id": "A", "p": 0.9},
                {"action_id": "B", "p": 0.6},
            ],
            "probability_policy": {
                "requires_normalization": True,
                "epsilon": 0.0001,
                "on_violation": "normalize",
            },
        }
        audits: list[str] = []
        errors = _apply_contract_policy("ipw_v1", payload, audits, mode="strict")
        self.assertEqual(errors, [])
        self.assertAlmostEqual(sum(row["p"] for row in payload["predictions"]), 1.0, places=6)
        self.assertTrue(audits)
        self.assertIn("ipw_validation.audit.normalized=true", audits[0])
        self.assertIn("ipw_validation.audit.original_sum=", audits[0])


if __name__ == "__main__":
    unittest.main()
