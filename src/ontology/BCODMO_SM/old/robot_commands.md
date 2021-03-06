# Run templates

## Biology
Run anatomy.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template biology/robot_templates/anatomy.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "COB:http://purl.obolibrary.org/obo/COB_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_"  --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/biology/robot_templates/anatomy.owl" -o biology/robot_templates/anatomy.owl
```

Run ecology.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template biology/robot_templates/ecology.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "ENVO:http://purl.obolibrary.org/obo/ENVO_" --prefix "PCO:http://purl.obolibrary.org/obo/PCO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_"  --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/biology/robot_templates/ecology.owl" -o biology/robot_templates/ecology.owl
```



Run physiology.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template biology/robot_templates/physiology.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_"  --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/biology/robot_templates/physiology.owl" -o biology/robot_templates/physiology.owl
```

## Quantifiers
Run quantifiers.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template quantifiers/robot_templates/quantifiers.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --prefix "SIO:http://semanticscience.org/resource/SIO_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/quantifiers/robot_templates/quantifiers.owl" -o quantifiers/robot_templates/quantifiers.owl
```




## Chemistry
Run element.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template chemistry/robot_templates/element.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/chemistry/robot_templates/element.owl" -o chemistry/robot_templates/element.owl
```

Run compound.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template chemistry/robot_templates/compound.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/chemistry/robot_templates/compound.owl" -o chemistry/robot_templates/compound.owl
```

## Physics
Run characteristic.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template physics/robot_templates/characteristic.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/physics/robot_templates/characteristic.owl" -o physics/robot_templates/characteristic.owl
```

Run phenomenon.tsv run from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template physics/robot_templates/phenomenon.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --prefix "SIO:http://semanticscience.org/resource/SIO_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/physics/robot_templates/phenomenon.owl" -o physics/robot_templates/phenomenon.owl
```

### Matrix
Run material.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template matrix/robot_templates/material.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/robot_templates/material.owl" -o matrix/robot_templates/material.owl
```

Run context.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template matrix/robot_templates/context.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/robot_templates/context.owl" -o matrix/robot_templates/context.owl
```

Run biome.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template matrix/robot_templates/biome.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/robot_templates/biome.owl" -o matrix/robot_templates/biome.owl
```

Run region.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template matrix/robot_templates/region.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/robot_templates/region.owl" -o matrix/robot_templates/region.owl
```

## Operational
Run operational.tsv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template operational/robot_templates/operational.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/operational/robot_templates/operational.owl" -o operational/robot_templates/operational.owl
```

## Units
Run uo_simplified.csv from `bcodmont/src/ontology/BCODMO_SM/`
```
robot template --template units/robot_templates/uo_simplified.csv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "UO:http://purl.obolibrary.org/obo/UO_" --ontology-iri "http://purl.obolibrary.org/obo/uo.owl" -o units/uo_simplified.owl
```

# Merge templates

### Merge imports and preliminary robot templates

Run from `bcodmont/src/ontology/BCODMO_SM/` This is for modules other than chemistry (where we are not removing CHEBIs axioms).
```
robot merge --input ../imports/envo_import.owl --input ../imports/pato_import.owl --input ../imports/uberon_import.owl --input ../imports/go_import.owl --input ../imports/iao_import.owl --input ../imports/obi_import.owl --input ../imports/uo_import.owl --input ../imports/chebi_import.owl --input ../imports/stato_import.owl --input ../imports/ms_import.owl --input ../imports/bfo_import.owl --input ../imports/cl_import.owl --input biology/robot_templates/physiology.owl --input physics/robot_templates/characteristic.owl --input physics/robot_templates/phenomenon.owl --input quantifiers/robot_templates/quantifiers.owl --input operational/robot_templates/operational.owl annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/merge_products/BCODMO_SM_merged.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/merge_products/BCODMO_SM_merged.owl" --output merge_products/BCODMO_SM_merged.owl
```

### Make object property free version of CHEBI.
We could add others here in future. Only run after adding to CHEBI import.
```
robot remove --input ../imports/chebi_import.owl --axioms logical annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/intermediate/chebi_import_axioms_removed.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/intermediate/chebi_import_axioms_removed.owl" --output intermediate/chebi_import_axioms_removed.owl
```

### Make object property free version of ENVO
Only run after adding to ENVO import.
```
robot remove --input ../imports/envo_import.owl --axioms logical annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/intermediate/envo_import_axioms_removed.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/intermediate/envo_import_axioms_removed.owl" --output intermediate/envo_import_axioms_removed.owl
```

### Make object property free version of UBERON
Only run after adding to UBERON import.
```
robot remove --input ../imports/uberon_import.owl --axioms logical annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/intermediate/uberon_import_axioms_removed.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/intermediate/uberon_import_axioms_removed.owl" --output intermediate/uberon_import_axioms_removed.owl
```

### Make object property free version of GO
Only run after adding to GO import.
```
robot remove --input ../imports/go_import.owl --axioms logical annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/intermediate/go_import_axioms_removed.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/intermediate/go_import_axioms_removed.owl" --output intermediate/go_import_axioms_removed.owl
```

## Merge modules with axiom removed ontologies

Modules include: both chemistry modules, all four matrix modules, biology ...
Axiom free ontologies include CHEBI, ENVO, IAO (for APs), UBERON, GO ...
Note adding IAO here didn't solve the issue of def and editor note not showing up. will need to fix this.
```
robot merge --input intermediate/chebi_import_axioms_removed.owl --input intermediate/envo_import_axioms_removed.owl --input intermediate/uberon_import_axioms_removed.owl --input intermediate/go_import_axioms_removed.owl --input ../imports/iao_import.owl --input ../imports/cl_import.owl --input biology/robot_templates/anatomy.owl --input biology/robot_templates/physiology.owl --input chemistry/robot_templates/element.owl --input chemistry/robot_templates/compound.owl --input matrix/robot_templates/material.owl --input matrix/robot_templates/context.owl --input matrix/robot_templates/biome.owl --input matrix/robot_templates/region.owl annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/merge_products/BCODMO_SM_axioms_removed_merged.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/merge_products/BCODMO_SM_axioms_removed_merged.owl" --output merge_products/BCODMO_SM_axioms_removed_merged.owl
```



# Filter to create export products

## Biology
Filter anatomy from axiom-free merged ontology
```
robot filter --input merge_products/BCODMO_SM_axioms_removed_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:anatomy" --select annotations --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/biology/anatomy.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/biology/anatomy.owl" --output biology/anatomy.owl
```

Filter physiology from axiom-free merged ontology
```
robot filter --input merge_products/BCODMO_SM_axioms_removed_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:physiology" --select annotations --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/biology/physiology.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/biology/physiology.owl" --output biology/physiology.owl
```

## Quantifiers
Filter quantifiers from merged ontology
```
robot filter --input merge_products/BCODMO_SM_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:quantifiers" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/quantifiers/quantifiers.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/quantifiers/quantifiers.owl" --output quantifiers/quantifiers.owl
```



## Chemistry
Filter element from axiom-free merged ontology
```
robot filter --input merge_products/BCODMO_SM_axioms_removed_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:element" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/chemistry/element.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/chemistry/element.owl" --output chemistry/element.owl
```

Filter compound from axiom-free merged ontology
```
robot filter --input merge_products/BCODMO_SM_axioms_removed_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:compound" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/chemistry/compound.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/chemistry/compound.owl" --output chemistry/compound.owl
```

## Physics
Filter characteristic from merged ontology
```
robot filter --input merge_products/BCODMO_SM_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:characteristic" --select annotations --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/physics/characteristic.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/physics/characteristic.owl" --output physics/characteristic.owl
```

Filter phenomenon from merged ontology
```
robot filter --input merge_products/BCODMO_SM_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:phenomenon" --select annotations --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/physics/phenomenon.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/physics/phenomenon.owl" --output physics/phenomenon.owl
```

## Matrix
Filter material from merged ontology
```
robot filter --input merge_products/BCODMO_SM_axioms_removed_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:material" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/material.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/material.owl" --output matrix/material.owl
```

Filter context from merged ontology
```
robot filter --input merge_products/BCODMO_SM_axioms_removed_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:context" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/context.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/context.owl" --output matrix/context.owl
```

Filter biome from merged ontology
```
robot filter --input merge_products/BCODMO_SM_axioms_removed_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:biome" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/biome.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/biome.owl" --output matrix/biome.owl
```

Filter region from merged ontology
```
robot filter --input merge_products/BCODMO_SM_axioms_removed_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:region" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/region.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/matrix/region.owl" --output matrix/region.owl
```

## Operational
Filter operational from merged ontology
```
robot filter --input merge_products/BCODMO_SM_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:operational" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/operational/operational.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/operational/operational.owl" --output operational/operational.owl
```




# Export formats:

Available using Robot.
`robot convert --input qualifiers/qualifiers.owl --output exports/qualifiers_robot.json`
`robot convert --input qualifiers/qualifiers.owl --output exports/qualifiers_robot.obo`
`robot convert --input qualifiers/qualifiers.owl --output exports/qualifiers_robot.ofn`
`robot convert --input qualifiers/qualifiers.owl --output exports/qualifiers_robot.omn`
`robot convert --input qualifiers/qualifiers.owl --output exports/qualifiers_robot.owl`
`robot convert --input qualifiers/qualifiers.owl --output exports/qualifiers_robot.owx`
`robot convert --input qualifiers/qualifiers.owl --output exports/qualifiers_robot.ttl`

## owl2vowl module to get to json
```
java -jar exports/util/owl2vowl.jar -file qualifiers/qualifiers.owl && mv qualifiers.json exports/qualifiers_owl2vowl.json
```



# OLD

Run qualifiers.tsv
```
## Run qualifiers.tsv run from bcodmont/src/ontology/BCODMO_SM/
robot template --template qualifiers/robot_templates/qualifiers.tsv -i ../bcodmont-edit.owl --prefix "RO:http://purl.obolibrary.org/obo/RO_" --prefix "BSM:http://purl.obolibrary.org/obo/BSM_" --prefix "SIO:http://semanticscience.org/resource/SIO_" --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/qualifiers/robot_templates/qualifiers.owl" -o qualifiers/robot_templates/qualifiers.owl
```
Filter qualifiers.tsv
```
### Qualifiers
## Filter qualifiers from merged ontology
robot filter --input merge_products/BCODMO_SM_merged.owl --prefix "bsm:http://bcodmo/sm#" --select "oboInOwl:inSubset=bsm:qualifiers" --select annotations  --signature true annotate --ontology-iri "http://purl.obolibrary.org/BCODMO_SM/qualifiers/qualifiers.owl" --version-iri "http://purl.obolibrary.org/BCODMO_SM/qualifiers/qualifiers.owl" --output qualifiers/qualifiers.owl
```
