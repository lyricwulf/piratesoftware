import polars as pl
import io

df = pl.read_csv(io.StringIO("""Date,Channel,Type,Amount
"9:56 PM PDT Aug 31, 2018",PirateSoftware,Cheering,50 Bits
"9:54 PM PDT Sep 25, 2018",PirateSoftware,Cheering,50 Bits
"9:53 PM PDT Oct 4, 2018",PirateSoftware,Cheering,50 Bits
"9:39 PM PDT Aug 15, 2018",PirateSoftware,Cheering,13 Bits
"9:37 PM PDT Aug 15, 2018",PirateSoftware,Cheering,50 Bits
"9:36 PM PDT Aug 15, 2018",PirateSoftware,Cheering,50 Bits
"9:34 PM PDT Aug 30, 2018",PirateSoftware,Cheering,3 Bits
"9:33 PM PDT Aug 30, 2018",PirateSoftware,Cheering,21 Bits
"9:26 PM PDT Sep 3, 2018",PirateSoftware,Cheering,50 Bits
"9:25 PM PDT Aug 25, 2018",PirateSoftware,Cheering,1 Bit
"9:24 PM PDT Sep 29, 2018",PirateSoftware,Cheering,50 Bits
"9:23 PM PDT Aug 25, 2018",PirateSoftware,Cheering,1 Bit
"9:21 PM PDT Aug 25, 2018",PirateSoftware,Cheering,1 Bit
"9:20 PM PDT Aug 25, 2018",PirateSoftware,Cheering,30 Bits
"9:15 PM PDT Sep 29, 2018",PirateSoftware,Cheering,100 Bits
"9:11 PM PDT Sep 2, 2018",PirateSoftware,Cheering,50 Bits
"9:07 PM PDT Oct 1, 2018",PirateSoftware,Cheering,100 Bits
"8:57 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:41 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:40 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:40 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:39 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:39 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:38 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:35 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:28 PM PDT Sep 29, 2018",PirateSoftware,Cheering,50 Bits
"8:27 PM PDT Sep 29, 2018",PirateSoftware,Cheering,50 Bits
"8:27 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:25 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:24 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:24 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:12 PM PDT Aug 26, 2018",PirateSoftware,Cheering,10 Bits
"8:10 PM PDT Aug 26, 2018",PirateSoftware,Cheering,1 Bit
"8:10 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"8:09 PM PDT Aug 26, 2018",PirateSoftware,Cheering,1 Bit
"7:37 PM PDT Sep 16, 2018",PirateSoftware,Cheering,50 Bits
"7:31 PM PDT Aug 19, 2018",PirateSoftware,Cheering,50 Bits
"7:29 PM PDT Aug 19, 2018",PirateSoftware,Cheering,50 Bits
"7:24 PM PDT Aug 19, 2018",PirateSoftware,Cheering,100 Bits
"7:24 PM PDT Aug 19, 2018",PirateSoftware,Cheering,100 Bits
"7:04 PM PDT Oct 5, 2018",PirateSoftware,Cheering,20 Bits
"7:03 PM PDT Oct 5, 2018",PirateSoftware,Cheering,5 Bits
"7:03 PM PDT Oct 5, 2018",PirateSoftware,Cheering,20 Bits
"7:02 PM PDT Oct 5, 2018",PirateSoftware,Cheering,50 Bits
"7:02 PM PDT Oct 5, 2018",PirateSoftware,Cheering,50 Bits
"7:02 PM PDT Oct 5, 2018",PirateSoftware,Cheering,20 Bits
"7:01 PM PDT Oct 5, 2018",PirateSoftware,Cheering,20 Bits
"7:00 PM PDT Oct 5, 2018",PirateSoftware,Cheering,50 Bits
"6:48 PM PDT Sep 2, 2018",PirateSoftware,Cheering,50 Bits
"6:24 PM PDT Aug 14, 2018",PirateSoftware,Cheering,50 Bits
"6:06 PM PDT Sep 2, 2018",PirateSoftware,Cheering,50 Bits
"6:06 PM PDT Sep 2, 2018",PirateSoftware,Cheering,50 Bits
"6:03 PM PDT Aug 14, 2018",PirateSoftware,Cheering,50 Bits
"5:53 PM PDT Sep 23, 2018",PirateSoftware,Cheering,5 Bits
"5:44 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"5:43 PM PDT Sep 22, 2018",PirateSoftware,Cheering,3 Bits
"5:43 PM PDT Sep 22, 2018",PirateSoftware,Cheering,2 Bits
"5:43 PM PDT Sep 22, 2018",PirateSoftware,Cheering,2 Bits
"5:43 PM PDT Sep 22, 2018",PirateSoftware,Cheering,1 Bit
"5:38 AM PDT Sep 19, 2018",PirateSoftware,Cheering,50 Bits
"5:12 AM PDT Sep 19, 2018",PirateSoftware,Cheering,50 Bits
"5:05 AM PDT Sep 19, 2018",PirateSoftware,Cheering,5 Bits
"4:58 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"4:55 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"4:54 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"4:54 PM PDT Aug 27, 2018",PirateSoftware,Cheering,10 Bits
"4:50 PM PDT Sep 2, 2018",PirateSoftware,Cheering,50 Bits
"4:45 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"4:43 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"4:42 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"4:39 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"4:34 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits
"4:29 PM PDT Sep 18, 2018",PirateSoftware,Cheering,6 Bits
"4:26 PM PDT Sep 28, 2018",PirateSoftware,Cheering,50 Bits
"4:02 PM PDT Aug 14, 2018",PirateSoftware,Cheering,1 Bit
"4:02 PM PDT Aug 14, 2018",PirateSoftware,Cheering,1 Bit
"4:02 PM PDT Aug 14, 2018",PirateSoftware,Cheering,1 Bit
"4:02 PM PDT Aug 14, 2018",PirateSoftware,Cheering,1 Bit
"4:02 PM PDT Aug 14, 2018",PirateSoftware,Cheering,1 Bit
"3:58 PM PDT Aug 14, 2018",PirateSoftware,Cheering,50 Bits
"3:58 PM PDT Aug 14, 2018",PirateSoftware,Cheering,25 Bits
"3:57 PM PDT Aug 14, 2018",PirateSoftware,Cheering,75 Bits
"3:57 PM PDT Aug 14, 2018",PirateSoftware,Cheering,75 Bits
"3:57 PM PDT Aug 14, 2018",PirateSoftware,Cheering,50 Bits
"3:57 PM PDT Aug 14, 2018",PirateSoftware,Cheering,125 Bits
"3:57 PM PDT Aug 14, 2018",PirateSoftware,Cheering,100 Bits
"3:57 PM PDT Aug 14, 2018",PirateSoftware,Cheering,100 Bits
"3:54 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:52 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:50 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:49 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:48 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:47 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:46 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:46 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:43 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:38 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:35 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:34 PM PST Dec 12, 2018",PirateSoftware,Cheering,100 Bits
"3:34 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:33 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:32 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:29 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:21 PM PDT Oct 7, 2018",PirateSoftware,Cheering,50 Bits
"3:13 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"3:13 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"3:12 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"3:08 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"3:04 PM PDT Sep 21, 2018",PirateSoftware,Cheering,50 Bits
"3:00 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:58 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:58 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:56 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:47 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:46 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:43 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits
"2:42 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:38 PM PDT Sep 23, 2018",PirateSoftware,Cheering,1 Bit
"2:36 PM PDT Aug 28, 2018",PirateSoftware,Cheering,5 Bits
"2:26 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits
"2:22 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:21 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:20 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:20 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:19 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits
"2:16 PM PDT Aug 25, 2018",PirateSoftware,Cheering,50 Bits
"2:14 PM PDT Sep 2, 2018",PirateSoftware,Cheering,50 Bits
"2:03 PM PDT Sep 15, 2018",PirateSoftware,Cheering,50 Bits
"12:58 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits
"12:57 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits
"12:57 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits
"12:56 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits
"12:54 PM PDT Sep 22, 2018",PirateSoftware,Cheering,18 Bits
"12:47 AM PDT Sep 21, 2018",PirateSoftware,Cheering,50 Bits
"12:45 PM PDT Oct 5, 2018",PirateSoftware,Cheering,25 Bits
"12:45 PM PDT Oct 5, 2018",PirateSoftware,Cheering,20 Bits
"12:44 PM PDT Sep 2, 2018",PirateSoftware,Cheering,50 Bits
"12:44 PM PDT Oct 5, 2018",PirateSoftware,Cheering,5 Bits
"12:44 PM PDT Oct 5, 2018",PirateSoftware,Cheering,20 Bits
"12:43 PM PDT Oct 5, 2018",PirateSoftware,Cheering,100 Bits
"12:42 PM PDT Oct 5, 2018",PirateSoftware,Cheering,25 Bits
"12:42 PM PDT Oct 5, 2018",PirateSoftware,Cheering,10 Bits
"12:41 PM PDT Oct 5, 2018",PirateSoftware,Cheering,25 Bits
"12:41 PM PDT Oct 5, 2018",PirateSoftware,Cheering,20 Bits
"12:40 PM PDT Oct 5, 2018",PirateSoftware,Cheering,20 Bits
"12:25 PM PDT Sep 9, 2018",PirateSoftware,Cheering,400 Bits
"12:21 PM PDT Aug 17, 2018",PirateSoftware,Cheering,1 Bit
"12:19 PM PDT Aug 20, 2018",PirateSoftware,Cheering,50 Bits
"12:06 AM PDT Sep 22, 2018",PirateSoftware,Cheering,50 Bits
"11:57 AM PDT Sep 23, 2018",PirateSoftware,Cheering,10 Bits
"11:52 PM PDT Oct 3, 2018",PirateSoftware,Cheering,50 Bits
"11:51 PM PDT Sep 18, 2018",PirateSoftware,Cheering,50 Bits
"11:51 AM PDT Sep 23, 2018",PirateSoftware,Cheering,10 Bits
"11:50 PM PDT Oct 3, 2018",PirateSoftware,Cheering,50 Bits
"11:49 AM PDT Sep 23, 2018",PirateSoftware,Cheering,16 Bits
"11:47 PM PDT Sep 18, 2018",PirateSoftware,Cheering,50 Bits
"11:47 PM PDT Oct 3, 2018",PirateSoftware,Cheering,50 Bits
"11:46 PM PDT Oct 3, 2018",PirateSoftware,Cheering,50 Bits
"11:44 PM PDT Oct 2, 2018",PirateSoftware,Cheering,50 Bits
"11:37 PM PDT Sep 25, 2018",PirateSoftware,Cheering,50 Bits
"11:25 PM PDT Sep 2, 2018",PirateSoftware,Cheering,"1,000 Bits"
"11:17 PM PDT Oct 20, 2018",PirateSoftware,Cheering,5 Bits
"11:07 PM PDT Sep 20, 2018",PirateSoftware,Cheering,150 Bits
"10:51 PM PDT Sep 20, 2018",PirateSoftware,Cheering,50 Bits
"10:50 PM PDT Aug 18, 2018",PirateSoftware,Cheering,42 Bits
"10:45 PM PDT Sep 20, 2018",PirateSoftware,Cheering,50 Bits
"10:40 PM PDT Aug 20, 2018",PirateSoftware,Cheering,"1,000 Bits"
"10:39 PM PDT Sep 21, 2018",PirateSoftware,Cheering,50 Bits
"10:39 PM PDT Sep 20, 2018",PirateSoftware,Cheering,150 Bits
"10:39 PM PDT Aug 20, 2018",PirateSoftware,Cheering,100 Bits
"10:36 PM PDT Sep 20, 2018",PirateSoftware,Cheering,50 Bits
"10:32 PM PDT Sep 20, 2018",PirateSoftware,Cheering,50 Bits
"10:31 PM PDT Sep 20, 2018",PirateSoftware,Cheering,50 Bits
"10:29 PM PDT Sep 21, 2018",PirateSoftware,Cheering,50 Bits
"10:26 PM PDT Sep 21, 2018",PirateSoftware,Cheering,50 Bits
"10:24 PM PDT Sep 21, 2018",PirateSoftware,Cheering,50 Bits
"10:22 PM PDT Sep 21, 2018",PirateSoftware,Cheering,50 Bits
"10:15 PM PDT Sep 21, 2018",PirateSoftware,Cheering,50 Bits
"10:05 PM PDT Aug 30, 2018",PirateSoftware,Cheering,2 Bits
"1:59 PM PDT Sep 15, 2018",PirateSoftware,Cheering,50 Bits
"1:52 PM PDT Sep 15, 2018",PirateSoftware,Cheering,50 Bits
"1:51 PM PDT Sep 15, 2018",PirateSoftware,Cheering,1 Bit
"1:47 PM PDT Sep 15, 2018",PirateSoftware,Cheering,50 Bits
"1:23 PM PDT Sep 15, 2018",PirateSoftware,Cheering,50 Bits
"1:20 AM PDT Sep 5, 2018",PirateSoftware,Cheering,10 Bits
"1:09 PM PDT Sep 23, 2018",PirateSoftware,Cheering,5 Bits
"1:03 PM PDT Oct 6, 2018",PirateSoftware,Cheering,50 Bits"""))

df = df.with_columns(
    Date=pl.col("Date").str.strptime(pl.Datetime, "%-I:%M %p %Z %b %-d, %Y")
).sort(
    "Date"
).with_columns(
    Date=pl.col("Date").dt.strftime("%Y %b %-d, %H:%M PDT") 
)

csv_string = df.write_csv(None)

csv_string