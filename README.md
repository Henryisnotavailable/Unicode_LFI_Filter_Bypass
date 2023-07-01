# Unicode_LFI_Filter_Bypass
This script will read user input and convert a set of characters into a unicode format, that is then percent-encoded.

#Why
If the backend of a server is performing input validation, like checking for ../ sequences this script could be used to bypass it.
This script matches the .. and / characters and converts them to a unicode character, that when normalised will return to the original character, bypassing the filter.

Based on this good article https://jlajara.gitlab.io/Bypass_WAF_Unicode
