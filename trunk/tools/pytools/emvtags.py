#
# EMV card tag library
#
# Ben Adida <ben@mit.edu>
# Steven J. Murdoch <http://www.cl.cam.ac.uk/~sjm217/>
#

TAGS= {}

TAGS["4F"] = "Application Identifier (AID)"
TAGS["50"] = "Application Label"
TAGS["57"] = "Track 2 Equivalent Data"
TAGS["5A"] = "Primary Account Number (PAN)"
TAGS["5F20"] = "Cardholder Name"
TAGS["5F24"] = "Application Expiration Date" 
TAGS["5F25"] = "Application Effective Date"
TAGS["5F28"] = "Issuer Country Code" 
TAGS["5F2A"] = "Transaction Currency Code"
TAGS["5F2D"] = "Language Preference"
TAGS["5F30"] = "Service Code"
TAGS["5F34"] = "PAN Sequence Number"
TAGS["5F36"] = "Transaction Currency Exponent"
TAGS["61"] = "Application Template"
TAGS["6F"] = "File Control Information (FCI) Template"
TAGS["70"] = "Application Elementary File (AEF) Data Template"
TAGS["71"] = "Issuer Script Template 1"
TAGS["72"] = "Issuer Script Template 2"
TAGS["73"] = "Directory Discretionary Template"
TAGS["77"] = "Response Message Template Format 2"
TAGS["80"] = "Response Message Template Format 1"
TAGS["81"] = "Amount, Authorised (Binary)"
TAGS["82"] = "Application Interchange Profile"
TAGS["83"] = "Command Template"
TAGS["84"] = "Dedicated File (DF) Name"
TAGS["86"] = "Issuer Script Command"
TAGS["87"] = "Application Priority Indicator"
TAGS["88"] = "Short File Identifier (SFI)"
TAGS["89"] = "Authorisation Code"
TAGS["8A"] = "Authorisation Response Code"
TAGS["8C"] = "Card Risk Management Data Object List 1 (CDOL1)"
#TAGS["8D"] = ["Card Risk Management Data Object List 2 (CDOL2)", False]
TAGS["8D"] = "Card Risk Management Data Object List 2 (CDOL2)"
TAGS["8E"] = "Cardholder Verification Method (CVM) List"
TAGS["8F"] = "Certification Authority Public Key Index"
TAGS["90"] = "Issuer Public Key Certificate"
TAGS["91"] = "Issuer Authentication Data"
TAGS["92"] = "Issuer Public Key Remainder"
TAGS["93"] = "Signed Static Application Data"
TAGS["94"] = "Application File Locator (AFL)"
TAGS["95"] = "Terminal Verification Results"
TAGS["97"] = "Transaction Certificate Data Object List (TDOL)"
TAGS["98"] = "Transaction Certificate (TC) Hash Value"
TAGS["99"] = "Transaction PIN Data"
TAGS["9A"] = "Transaction Date"
TAGS["9B"] = "Transaction Status Information"
TAGS["9C"] = "Transaction Type"
TAGS["9D"] = "Directory Definition File (DDF) Name"
TAGS["9F01"] = "Acquirer Identifier"
TAGS["9F02"] = "Amount, Authorised (Numeric)"
TAGS["9F03"] = "Amount, Other (Numeric)"
TAGS["9F04"] = "Amount, Other (Binary)"
TAGS["9F05"] = "Application Discretionary Data"
TAGS["9F06"] = "Application Identifier (AID)"
TAGS["9F07"] = "Application Usage Control"
TAGS["9F08"] = "Application Version Number"
TAGS["9F09"] = "Application Version Number"
TAGS["9F0B"] = "Cardholder Name -Extended"
TAGS["9F0D"] = "Issuer Action Code - Default"
TAGS["9F0E"] = "Issuer Action Code - Denial"
TAGS["9F0F"] = "Issuer Action Code - Online"
TAGS["9F10"] = "Issuer Application Data"
TAGS["9F11"] = "Issuer Code Table Index"
TAGS["9F12"] = "Application Preferred Name"
TAGS["9F13"] = "Last Online Application Transaction Counter (ATC) Register"
TAGS["9F14"] = "Lower Consecutive Offline Limit"
TAGS["9F15"] = "Merchant Category Code"
TAGS["9F16"] = "Merchant Identifier"
TAGS["9F17"] = "Personal Identification Number (PIN) Try Counter"
TAGS["9F18"] = "Issuer Script Identifier"
TAGS["5F50"] = "Issuer URL"
TAGS["9F1A"] = "Terminal Country Code"
TAGS["9F1B"] = "Terminal Floor Limit"
TAGS["9F1C"] = "Terminal Identification"
TAGS["9F1D"] = "Terminal Risk Management Data"
TAGS["9F1E"] = "Interface Device (IFD) Serial Number"
TAGS["9F1F"] = "Track 1 Discretionary Data"
TAGS["9F20"] = "Track 2 Discretionary Data"
TAGS["9F21"] = "Transaction Time"
TAGS["9F22"] = "Certification Authority Public Key Index"
TAGS["9F23"] = "Upper Consecutive Offline Limit"
TAGS["9F26"] = "Application Cryptogram"
TAGS["9F27"] = "Cryptogram Information Data"
TAGS["9F2D"] = "ICC PIN Encipherment Public Key Certificate"
TAGS["9F2E"] = "ICC PIN Encipherment Public Key Exponent"
TAGS["9F2F"] = "ICC PIN Encipherment Public Key Remainder"
TAGS["9F32"] = "Issuer Public Key Exponent"
TAGS["9F33"] = "Terminal Capabilities"
TAGS["9F34"] = "Cardholder Verification Method (CVM) Results"
TAGS["9F35"] = "Terminal Type"
TAGS["9F36"] = "Application Transaction Counter (ATC)"
TAGS["9F37"] = "Unpredictable Number"
TAGS["9F38"] = "Processing Options Data Object List (PDOL)"
TAGS["9F39"] = "Point-of-Service (POS) Entry Mode"
TAGS["9F3A"] = "Amount, Reference Currency"
TAGS["9F3B"] = "Application Reference Currency"
TAGS["9F3C"] = "Transaction Reference Currency"
TAGS["9F3D"] = "Transaction Reference Currency Exponent"
TAGS["9F40"] = "Additional Terminal Capabilities"
TAGS["9F41"] = "Transaction Sequence Counter"
TAGS["9F42"] = "Application Currency Code"
TAGS["9F43"] = "Application Reference Currency Exponent"
TAGS["9F44"] = "Application Currency Exponent"
TAGS["9F45"] = "Data Authentication Code"
TAGS["9F46"] = "ICC Public Key Certificate"
TAGS["9F47"] = "ICC Public Key Exponent"
TAGS["9F48"] = "ICC Public Key Remainder"
TAGS["9F49"] = "Dynamic Data Object List (DDOL)"
TAGS["9F4A"] = "Static Data Authentication Tag List"
TAGS["9F4B"] = "Signed Dynamic Application Data"
TAGS["9F4C"] = "ICC Dynamic Number"
TAGS["A5"] = "FCI Proprietary Template"
TAGS["BF0C"] = "FCI Issuer Discretionary Data"

## From BoS CAP compatible card
TAGS["9F56"] = "CAP ARQC bit filter"
TAGS["9F55"] = "CAP (unknown)"

def tagname(tag):
    if tag in TAGS: return TAGS[tag]
    return 'Unknown'