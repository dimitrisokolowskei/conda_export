configfile: "config.yaml"

rule all:
  input:
    expand("raw_qc/{sample}_{replicate}.fastqc.{extension}", sample=config["sample"], replicate=[1, 2], extension=["zip", "html"])

rule fastqc:
  input:
    rawread=expand("raw_data/{sample}_{replicate}.fastq.gz", sample=config["samples"], replicate=[1, 2])
  output:
    zip=expand("raw_qc/{sample}_{replicate}.fastqc.zip", sample=config["samples"], replicate=[1, 2])
    html=expand("raw_qc/{sample}_{replicate}.fastqc.html", sample=config["samples"], replicate=[1, 2])
  threads:
    6
  params:
    path="Filtered/"
  shell:
    "fastqc -t {threads} {input.rawread} -o {params.path}" 


