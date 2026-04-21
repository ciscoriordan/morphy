"""Pinned HuggingFace Hub revisions for reproducible installs.

Each Opla release pins the exact commit SHA of every external weight source
it downloads. This means:

- v0.2.0 installed today pulls the same blobs as v0.2.0 installed in a year,
  even if the upstream HF repos have been updated.
- Security: a compromised HF account can't silently swap weights under us.
- Reproducibility: benchmark numbers stay meaningful across time.

To cut a new Opla release that tracks updated upstream weights:
  1. Fetch the latest SHA for each repo (HF UI or `huggingface_hub.list_repo_refs`).
  2. Update the constants below.
  3. Re-run the slow test suite to confirm behavior.
  4. Bump Opla's version in opla/__init__.py.
"""

# AUEB-NLP's gr-nlp-toolkit checkpoint (pos_processor, dp_processor)
GR_NLP_TOOLKIT_REV = "5ddcf577a976b3402ba8810f181eea9ec202a70e"

# AUEB-NLP's GreekBERT backbone (Modern Greek)
GREEK_BERT_REV = "ec2b8f88dd215b5246f2f850413d5bff90d7540d"

# Pranaydeep Singh's Ancient-Greek-BERT backbone (grc + med)
ANCIENT_GREEK_BERT_REV = "5e3e29ece1d63029baa226f11105b1e8277c4f07"

# Opla's own trained AG/med heads
OPLA_WEIGHTS_REV = "d23dedbda2344bb94b6d0b8eb7c96a0d07692582"


BERT_REVISIONS = {
    "nlpaueb/bert-base-greek-uncased-v1": GREEK_BERT_REV,
    "pranaydeeps/Ancient-Greek-BERT": ANCIENT_GREEK_BERT_REV,
}
