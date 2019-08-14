# installing tca
library(devtools)
install_github("cozygene/TCA")

# load tca
library(TCA)

samples <- data.matrix(read.csv('samplesheet_colremoved.csv', row.names = 1))
meth_data <- data.matrix(read.csv('RAmeth_matrix_linesremoved_10Kmostvar.csv', row.names = 1))
pheno <- data.frame(t(samples))
k <- 6

ra <- pheno[,1, drop=FALSE]
covars <- pheno[,-1, drop=FALSE]


# houseman cell proportions from GLINT 
cell_proportions <- data.matrix(read.csv('cell_proportions_houseman.csv', row.names=1))

# use of tca
tca_output <- tca(meth_data, cell_proportions, C1=covars, C2=ra, refit_W=TRUE)

# write tca output to file
saveRDS(tca_output, file = "RA_TCAoutput.rds")
