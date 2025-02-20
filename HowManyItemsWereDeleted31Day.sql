SELECT 
      Count (case when (item.record_creation_date_gmt > (now() - interval '0 month')) and item.location_code like 'gm%' then 1 end) as "Holdings Prior Month Place Holder",
       Count (case when (item.record_creation_date_gmt > (now() - interval '31 day')) and item.location_code like 'gm%' then 1 end) as "TOTAL Main Created Last Month",
       count (case when item.location_code like 'gm%' then 1 end) as "TOTAL Owned at Main",
       count (case when BibRecProp.material_code = '@' and bib.record_creation_date_gmt > (now() - interval '31 day') then 1 end) as "New e-Book Bibs",
       count (case when BibRecProp.material_code = 'e' and bib.record_creation_date_gmt > (now() - interval '31 day') then 1 end) as "New Downloadable Audiobook Bibs",
       Count (case when (item.record_creation_date_gmt > (now() - interval '31 day')) and item.location_code like 'gmj%' then 1 end) as "New Juv Main Items",
      Count (case when (item.record_creation_date_gmt > (now() - interval '0 month')) and item.location_code like 'gb%' then 1 end) as "Holdings Prior Month Place Holder",
       Count (case when (item.record_creation_date_gmt > (now() - interval '31 day')) and item.location_code like 'gb%' then 1 end) as "TOTAL BYR Created Last Month",
       count (case when item.location_code like 'gb%' then 1 end) as "TOTAL Owned at BYR",
        Count (case when (item.record_creation_date_gmt > (now() - interval '31 day')) and item.location_code like 'gbj%' then 1 end) as "New BYR Juv Items ",      
              Count (case when (item.record_creation_date_gmt > (now() - interval '0 month')) and item.location_code like 'gc%' then 1 end) as "Holdings Prior Month Place Holder",
       Count (case when (item.record_creation_date_gmt > (now() - interval '31 day')) and item.location_code like 'gc%' then 1 end) as "TOTAL Cos Created Last Month",
       count (case when item.location_code like 'gc%' then 1 end) as "TOTAL Owned at Cos",
        Count (case when (item.record_creation_date_gmt > (now() - interval '31 day')) and item.location_code like 'gcj%' then 1 end) as "New COS Items" 
FROM 
  sierra_view.item_view as item
  join sierra_view.bib_record_item_record_link as BibItemLink on BibItemLink.item_record_id = item.id
  full outer join sierra_view.bib_view as BIB on BIB.id = BibItemLink.bib_record_id
  full outer Join sierra_view.bib_record_property as BibRecProp on BibRecProp.bib_record_id = bib.id; 