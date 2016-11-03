float_bill = float(input("What is the bill's total? ($x.yz) "))
float_taxPercent = float(input("What is the tax percentage? (x%) ")) / 100
float_tipPercent = float(input("What is the tip percentage? (x%) ")) / 100
print("\nBefore additional charges: $" + str("%.2f" % float_bill) + "\n" +
      "Tax (" + str(float_taxPercent) + "): $" + str("%.2f" % (float_bill * float_taxPercent)) + "\n" +
      "Tip (" + str(float_tipPercent) + "): $" + str("%.2f" % (float_bill * float_tipPercent)) + "\n" +
      "Bill total: $" + str("%.2f" % (float_bill + (float_bill * float_taxPercent) + (float_bill * float_tipPercent))))