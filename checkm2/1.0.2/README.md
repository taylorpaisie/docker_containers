# CheckM2

This image implements:
* [CheckM2 v1.0.2](hhttps://github.com/chklovski/CheckM2)

and can be accessed at [docker hub](https://hub.docker.com/repository/docker/tpaisie/checkm2/general).

## Example analysis
Get positive and negative control test data:
```
# Download positive and negative control test data
wget -nv --no-check-certificate https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_wgs.fa -O burk_wgs_pos_ctrl.fa
wget -nv --no-check-certificate https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_16S.fa -O burk_16S_neg_ctrl.fa

```

# Running CheckM2 on the test data
```
checkm2 predict --input burk_wgs_pos_ctrl.fa \
    burk_16S_neg_ctrl.fa \
    --output-directory tests_output/
```

## Run checksum on files
```
sha256sum burk_wgs_pos_ctrl.fa > burk_wgs_checksum.txt
sha256sum burk_16S_neg_ctrl.fa > burk_16S_checksum.txt
sha256sum tests_output/quality_report.tsv > quality_report_checksum.txt
```

