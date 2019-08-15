# installing tca
library(devtools)
install_github("cozygene/TCA")

# load tca
library(TCA)	

samples <- data.matrix(read.csv('samplesheet_colremoved.csv', row.names = 1))
meth_data <- data.matrix(read.csv('RAmeth_matrix_linesremoved_10Kmostvar.csv', row.names = 1))
pheno <- t(samples)
k <- 6

# MUST convert to matrix
ra <- matrix(pheno[,1, drop=FALSE])
covars <- matrix(pheno[,-1, drop=FALSE])


# houseman cell proportions from GLINT 
cell_proportions <- data.matrix(read.csv('cell_proportions_houseman.csv', row.names=1))

# use of tca
tca_model <- tca(meth_data, cell_proportions, C1=covars, C2=ra, refit_W=TRUE)

# write tca output to file
saveRDS(tca_output, file = "RA_TCAmodels.rds")

# re-load tca output
tca_model <-  readRDS(file="RA_TCAmodels.rds")

# fitting a tca regression model

tca_reg <- tcareg(meth_data, tca_model, ra, C3 = NULL, test = "marginal",
      null_model = NULL, alternative_model = NULL, save_results = TRUE,
      output = "TCA", sort_results = TRUE, parallel = FALSE,
      num_cores = NULL, log_file = "TCA.log", features_metadata = NULL,
      debug = TRUE)