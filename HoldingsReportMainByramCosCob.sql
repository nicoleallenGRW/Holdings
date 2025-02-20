SELECT 

  

count(case when location_code like 'gm%' and location_code not like 'gmj%' and (itype_code_num = '0' or itype_code_num = '6' or itype_code_num = '13') then 1 end) as "Main books 0",
count(case when location_code like 'gm%' and itype_code_num = '2' then 1 end) as "Music CDs 1",
count(case when location_code like 'gm%' and itype_code_num = '99' then 1 end) as "Music Downloadable 2",
count(case when location_code like 'gm%' and itype_code_num = '22' then 1 end) as "Audiobook CDs 3",
count(case when location_code like 'gm%' and itype_code_num = '99' then 1 end) as "Audiobook Downloadable 4",
count(case when location_code like 'gm%' and itype_code_num = '99' then 1 end) as "Video Downloadable 5",
count(case when location_code like 'gm%' and (itype_code_num = '44' or itype_code_num = '41') then 1 end) as "DVDs 6",
count(case when location_code like 'gm%' and itype_code_num = '7' then 1 end) as "Lending Art 7",
count(case when location_code like 'gm%' and itype_code_num = '18' then 1 end) as "Museum Passes 8",
count(case when location_code like 'gm%' and itype_code_num = '5' then 1 end) as "Innovation Lab Kits 9",
count(case when location_code like 'gm%' and itype_code_num = '62' then 1 end) as "Games 10",
count(case when location_code like 'gmj%' and (itype_code_num = '20' or itype_code_num = '6' or itype_code_num = '13') then 1 end) as "Juv Books 11",
count(case when location_code like 'gm%' and itype_code_num = '3' then 1 end) as "Juv Music CDs 12",
count(case when location_code like 'gm%' and itype_code_num = '23' then 1 end) as "Juv Audiobook 13",
count(case when location_code like 'gm%' and itype_code_num = '42' then 1 end) as "Juv DVDs 14",
count(case when location_code like 'gm%' and itype_code_num = '63' then 1 end) as "JUV Games 15",
count(case when location_code like 'gm%' and itype_code_num = '15' then 1 end) as "JUV Launchpads 15",

count(case when location_code like 'gb%' and location_code not like 'gbj%' and (itype_code_num = '0' or itype_code_num = '6' or itype_code_num = '13') then 1 end) as "Main books 16",
count(case when location_code like 'gb%' and itype_code_num = '2' then 1 end) as "Music CDs 17",
count(case when location_code like 'gb%' and itype_code_num = '99' then 1 end) as "Music Downloadable 18",
count(case when location_code like 'gb%' and itype_code_num = '22' then 1 end) as "Audiobook CDs 19",
count(case when location_code like 'gb%' and itype_code_num = '99' then 1 end) as "Audiobook Downloadable 21",
count(case when location_code like 'gb%' and itype_code_num = '99' then 1 end) as "Video Downloadable 22",
count(case when location_code like 'gb%' and (itype_code_num = '44' or itype_code_num = '41') then 1 end) as "DVDs 23",
count(case when location_code like 'gb%' and itype_code_num = '7' then 1 end) as "Lending Art 24",
count(case when location_code like 'gb%' and itype_code_num = '18' then 1 end) as "Museum Passes 25",
count(case when location_code like 'gb%' and itype_code_num = '5' then 1 end) as "Innovation Lab Kits 26",
count(case when location_code like 'gb%' and itype_code_num = '62' then 1 end) as "Games 27",
count(case when location_code like 'gbj%' and (itype_code_num = '20' or itype_code_num = '6' or itype_code_num = '13') then 1 end) as "Juv Books 11",
count(case when location_code like 'gb%' and itype_code_num = '3' then 1 end) as "Juv Music CDs 12",
count(case when location_code like 'gb%' and itype_code_num = '23' then 1 end) as "Juv Audiobook 13",
count(case when location_code like 'gb%' and itype_code_num = '42' then 1 end) as "Juv DVDs 14",
count(case when location_code like 'gb%' and itype_code_num = '63' then 1 end) as "JUV Games 15",
count(case when location_code like 'gb%' and itype_code_num = '15' then 1 end) as "JUV Launchpads 15",

count(case when location_code like 'gc%' and location_code not like 'gcj%' and (itype_code_num = '0' or itype_code_num = '6' or itype_code_num = '13') then 1 end) as "Main books 0",
count(case when location_code like 'gc%' and itype_code_num = '2' then 1 end) as "Music CDs 1",
count(case when location_code like 'gc%' and itype_code_num = '99' then 1 end) as "Music Downloadable 2",
count(case when location_code like 'gc%' and itype_code_num = '22' then 1 end) as "Audiobook CDs 3",
count(case when location_code like 'gc%' and itype_code_num = '99' then 1 end) as "Audiobook Downloadable 4",
count(case when location_code like 'gc%' and itype_code_num = '99' then 1 end) as "Video Downloadable 5",
count(case when location_code like 'gc%' and (itype_code_num = '44' or itype_code_num = '41') then 1 end) as "DVDs 6",
count(case when location_code like 'gc%' and itype_code_num = '7' then 1 end) as "Lending Art 7",
count(case when location_code like 'gc%' and itype_code_num = '18' then 1 end) as "Museum Passes 8",
count(case when location_code like 'gc%' and itype_code_num = '5' then 1 end) as "Innovation Lab Kits 9",
count(case when location_code like 'gc%' and itype_code_num = '62' then 1 end) as "Games 10",
count(case when location_code like 'gcj%' and (itype_code_num = '20' or itype_code_num = '6' or itype_code_num = '13') then 1 end) as "Juv Books 11",
count(case when location_code like 'gc%' and itype_code_num = '3' then 1 end) as "Juv Music CDs 12",
count(case when location_code like 'gc%' and itype_code_num = '23' then 1 end) as "Juv Audiobook 13",
count(case when location_code like 'gc%' and itype_code_num = '42' then 1 end) as "Juv DVDs 14",
count(case when location_code like 'gc%' and itype_code_num = '63' then 1 end) as "JUV Games 15",
count(case when location_code like 'gc%' and itype_code_num = '15' then 1 end) as "JUV Launchpads 15"


 
FROM 
  
  sierra_view.item_view;