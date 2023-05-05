import unittest

from linkml_transformer.utils.multi_file_transformer import MultiFileTransformer
from tests import EXAMPLE_DIR

EXAMPLE_PROJECTS = [
    "measurements",
    "flattening",
    "personinfo_basic",
    "type_coercion",
    "biolink",
]


class TransformerExamplesTestCase(unittest.TestCase):
    """
    Tests ObjectTransformer using examples.

    Assumes folder structures:

    - input/examples
       - {package}
          - source/{source_schema}.yaml  :: the schema to transform from
          - transform/{transform_spec}.transform.yaml :: mapping spec
          - data/{SourceClassName}-{LocalId}.yaml :: data to transform
          - target/{SourceClassName}-{LocalId}.yaml :: expected output data
    """

    def test_all(self):
        """
        Iterates through all examples.

        This uses the MultiFileProcessor in test_mode - if the outputs differ
        then the test will fail
        """
        mft = MultiFileTransformer()
        for directory in EXAMPLE_PROJECTS:
            full_dir = EXAMPLE_DIR / directory
            instructions = mft.infer_instructions(full_dir)
            mft.process_instructions(instructions, full_dir, test_mode=True)

    @unittest.skip("Uncomment this to regenerate examples")
    def test_regenerate(self):
        """
        Use this to regenerate test examples.
        """
        mft = MultiFileTransformer()
        dirs = EXAMPLE_PROJECTS
        for directory in dirs:
            full_dir = EXAMPLE_DIR / directory
            instructions = mft.infer_instructions(full_dir)
            # print(yaml.dump(instructions.dict()))
            mft.process_instructions(instructions, full_dir, test_mode=False)
