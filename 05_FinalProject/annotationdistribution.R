dat = read.csv("twokenizedcasesforR.csv")

table(dat$annotation)
which(dat$annotation=="s\342\200\232\303\204\302\266")
