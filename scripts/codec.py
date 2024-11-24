import codecs
import chardet

string = rb"\u9898\u76ee\u5df2\u5237\u65b0\uff0c\u8bf7\u91cd\u65b0\u7b54\u9898\u3002\u0669( \u2579\u25bf\u2579 )\u06f6"
print(
    "====================== String To Be Processed ======================\n",
    string,
    "\n",
)
detectedEncodeType = chardet.detect(string)
print(
    "==================== Auto-Detect Encoding Type =====================\n",
    detectedEncodeType,
    "\n",
)

decodedString = codecs.decode(string, detectedEncodeType["encoding"])

print(
    "========================= Decoded String ===========================\n",
    decodedString,
    "\n",
)
