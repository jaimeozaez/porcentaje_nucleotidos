# porcentaje_nucleotidos

**porcentaje_nucleotidos** is a script created to review a FASTA file and calculate the percentage of each nucleotide contained in every sequence in the file. In addition to displaying the result output on the terminal, a new text file is generated containing the data of the calculations performed.


## Script operation

The script includes a variable named **parametro_para_indicar_fichero_FASTA**, which is set as a empty string by default. This variable may be modified prior to the running of the script, specifying the directory and filename of the FASTA file to be processed. In case this variable remains empty, the script is designed to query the user for this information directly on the terminal (directory and filename).

```console
$ ¿El archivo FASTA se encuentra en el DIRECTORIO actual (ejemplo de ruta de directorio)? Responda (s/n).
$ Ingrese ruta del DIRECTORIO (no incluya la barra final):
$ Ingrese el nombre del ARCHIVO (incluya la extensión):
```

Once the script is executed, if no error is detected ( wrong directory or filename), the result of the percentage calculation for each of the nucleotides is displayed on the screen. The text file is generated, whose name will be the same as that of the original FASTA file, adding the tag "\_calculations.txt", and whose location is the same as that of the original FASTA file.
Finally, a message confirms the completion of the process.


---

For any clarification on the operation of the script, feel free to contact me through **_jaime.ozaez@gmail.com_**.
