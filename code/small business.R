rm(list=ls())
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
library(data.table)
small_business <- fread("Maryland SBDC Data 4 UMD Data Challenge 2019.csv", sep=",", header = TRUE, stringsAsFactors = TRUE)

for (i in columns(small_business)){
  print (levels(small_business$i)
  }
success <- small_business[`Impact: Started Business`=="Yes"&`Business Status`=="Started with SBDC"]
fail <- small_business[`Impact: Started Business`=="No"&`Business Status`=="Pre-venture/Nascent"]
SBDC <- small_business[`Business Status`=="Started with SBDC"]
a <- small_business[(`Business Status`=="In Business (> 1 year)"|`Business Status`=="Start-up (in bus. < 1 year)")&
  (`Impact: Started Business`=="Yes"|`Impact: Started Business`=="No")]





