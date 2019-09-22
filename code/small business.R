rm(list=ls())
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
library(data.table)
small_business <- fread("Maryland SBDC Data 4 UMD Data Challenge 2019.csv", sep=",", header = TRUE, stringsAsFactors = TRUE)

levels(small_business$`Service Center`)
levels(small_business$County)
levels(small_business$`Initial Services Sought at First Visit`)
levels(small_business$`Attended Group Training?`)
levels(small_business$`Business Status`)
levels(small_business$`Impact: Started Business`)
levels(small_business$`NAICS code`)
levels(small_business$`Ownership Gender`)
levels(small_business$`Owner's Hispanic Origin`)
levels(small_business$`Owner's Race`)

success <- small_business[`Impact: Started Business`=="Yes"&`Business Status`=="Started with SBDC"]
fail <- small_business[`Impact: Started Business`=="No"&`Business Status`=="Pre-venture/Nascent"]
SBDC <- small_business[`Business Status`=="Started with SBDC"]
a <- small_business[(`Business Status`=="In Business (> 1 year)"|`Business Status`=="Start-up (in bus. < 1 year)")&
  (`Impact: Started Business`=="Yes"|`Impact: Started Business`=="No")]





