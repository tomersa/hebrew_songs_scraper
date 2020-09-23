This repo scrapes hebrew songs from 3 different sites.

In order to run it you need to:
1. Run wget_all.sh - This script will start getting the html files from the different sites (After running this you'll see directory created for each site)
2. Wait a while so the script will start getting some html files to scrape.
3. Run scrape_all.sh - This script will scrape the html files and will output files with only the songs text (All in the same file) It will be named <site name>_output.txt

Check it out. You should see something similar to this:
הגבול הלגיטימי לגעגועים

(ככל דבר סכריני אחר)
עובר מן מחוזות השעמום וחבלי הנידחות 
לנפת הברירה נטולת הגבולות
של עולם הציד החופן בחובו
מועדון רוק אפלולי, נוטף זכרונות - 
זינוק עגול - ניענוע ירכיים - עיכוס קל
והשלכת השיער לאחור בתנועה חלקה של פרק היד
מונעים יצירת ספק - אצל

The scrapers might output 'Processing error' for some files. In this case it ignores it and continues to the next one. Not all files contain songs so this it not really a problem.
