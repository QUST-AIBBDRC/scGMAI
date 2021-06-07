library(SHARP)
brainTags <- read.csv("data.csv") 
brainTags <- brainTags[,-1]
a<-SHARP(brainTags)