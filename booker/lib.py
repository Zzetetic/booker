def calculate_pages(pages, sheet_in_block):
    pages_in_block = sheet_in_block * 4
    blocks = pages // pages_in_block
    remainder = pages % pages_in_block
    list_blocks = list()
    for i in range(blocks):
        left_page_in_block = i * pages_in_block + 1
        right_page_in_block = left_page_in_block + pages_in_block - 1
        list_pages_in_block = list()
        list_blocks.append(list_pages_in_block)
        
        for j in range(pages_in_block//2):
            pages_relation = dict()
            
            pages_relation['left_page'] = left_page_in_block + j
            pages_relation['right_page'] = right_page_in_block - j
            
            list_pages_in_block.append(pages_relation)
            
    if  remainder > 0:
        list_pages_in_block = list()
        list_blocks.append(list_pages_in_block)
         
        left_page_in_block = blocks * pages_in_block + 1
         
        for i in range(remainder):
            pages_relation = dict()
            pages_relation['left_page'] = left_page_in_block + i
            pages_relation['right_page'] = None
            list_pages_in_block.append(pages_relation)
   
    return list_blocks


