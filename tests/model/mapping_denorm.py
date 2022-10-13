# Auto generated from mapping_denorm.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-11T21:53:50
# Schema: mappings_norm
#
# id: https://w3id.org/linkml/examples/mappings-norm
# description: Normalized Mappings
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MAPPINGS = CurieNamespace('mappings', 'https://w3id.org/linkml/examples/mappings-norm/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://example.org/UNKNOWN/schema/')
SKOS = CurieNamespace('skos', 'http://example.org/UNKNOWN/skos/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MAPPINGS


# Types

# Class references



@dataclass
class MappingSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MAPPINGS.MappingSet
    class_class_curie: ClassVar[str] = "mappings:MappingSet"
    class_name: ClassVar[str] = "MappingSet"
    class_model_uri: ClassVar[URIRef] = MAPPINGS.MappingSet

    mappings: Optional[Union[Union[dict, "Mapping"], List[Union[dict, "Mapping"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.mappings, list):
            self.mappings = [self.mappings] if self.mappings is not None else []
        self.mappings = [v if isinstance(v, Mapping) else Mapping(**as_dict(v)) for v in self.mappings]

        super().__post_init__(**kwargs)


@dataclass
class Mapping(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MAPPINGS.Mapping
    class_class_curie: ClassVar[str] = "mappings:Mapping"
    class_name: ClassVar[str] = "Mapping"
    class_model_uri: ClassVar[URIRef] = MAPPINGS.Mapping

    subject_id: Optional[str] = None
    subject_name: Optional[str] = None
    object_id: Optional[str] = None
    object_name: Optional[str] = None
    predicate: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_id is not None and not isinstance(self.subject_id, str):
            self.subject_id = str(self.subject_id)

        if self.subject_name is not None and not isinstance(self.subject_name, str):
            self.subject_name = str(self.subject_name)

        if self.object_id is not None and not isinstance(self.object_id, str):
            self.object_id = str(self.object_id)

        if self.object_name is not None and not isinstance(self.object_name, str):
            self.object_name = str(self.object_name)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MAPPINGS.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=MAPPINGS.name, domain=None, range=Optional[str])

slots.predicate = Slot(uri=MAPPINGS.predicate, name="predicate", curie=MAPPINGS.curie('predicate'),
                   model_uri=MAPPINGS.predicate, domain=None, range=Optional[str])

slots.subject_id = Slot(uri=MAPPINGS.subject_id, name="subject_id", curie=MAPPINGS.curie('subject_id'),
                   model_uri=MAPPINGS.subject_id, domain=None, range=Optional[str])

slots.subject_name = Slot(uri=MAPPINGS.subject_name, name="subject_name", curie=MAPPINGS.curie('subject_name'),
                   model_uri=MAPPINGS.subject_name, domain=None, range=Optional[str])

slots.object_id = Slot(uri=MAPPINGS.object_id, name="object_id", curie=MAPPINGS.curie('object_id'),
                   model_uri=MAPPINGS.object_id, domain=None, range=Optional[str])

slots.object_name = Slot(uri=MAPPINGS.object_name, name="object_name", curie=MAPPINGS.curie('object_name'),
                   model_uri=MAPPINGS.object_name, domain=None, range=Optional[str])

slots.mappingSet__mappings = Slot(uri=MAPPINGS.mappings, name="mappingSet__mappings", curie=MAPPINGS.curie('mappings'),
                   model_uri=MAPPINGS.mappingSet__mappings, domain=None, range=Optional[Union[Union[dict, Mapping], List[Union[dict, Mapping]]]])
