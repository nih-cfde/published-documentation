# Building 'green' tables from core entity tables

This term-scanner script is used to auto-generate the green tables for the C2M2 Model [Level 1 model](https://github.com/nih-cfde/specifications-and-documentation/tree/master/draft-C2M2_specification_with_Levels#Level-1). Currently, this script generates four of the five green tables for Level 1. 

Default paths direct to the HMP example [tsv files](https://github.com/nih-cfde/specifications-and-documentation/tree/master/draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_1_bdbag.contents).

### Inputs
It currently takes in `biosample.tsv` and `file.tsv` (two of the core-entity ETL instance TSVs, aka two of the three black tables) from the `--draftDir` (default is `../draft-C2M2_example_submission_data/HMP__sample_C2M2_Level_1_bdbag.contents`)

It will load OBO and ontology files from `--cvRefDir` (default is `external_CV_reference_files`):
- `EDAM.version_1.21.tsv`
- `OBI.version_2019-08-15.obo`
- `uberon.version_2019-06-27.obo`

### Outputs
It will produce these four green tables for Level 1: `file_format.tsv`,`data_type.tsv`, `assay_type.tsv`, and `anatomy.tsv`. The outputs are saved in `--outDir` (default is `./007_HMP-specific_CV_term_usage_TSVs`). 

### Run script
The term-scanner script is named `build_term_tables.py` and you can run it like so:

```
# with default directory locations
./build_term_tables.py

# full command, if not using any default paths
./build_term_tables.py --draftDir [path/to/tsv/file/dir] --cvRefDir [path/to/external/CV/ref/files/dir] --outDir [dir/path/where/you/want/outputs/saved]
```
Run it with `-h` for command line help. 
