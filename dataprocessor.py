from pdfreader import read_pdf
from chunker import chunk_pages
from embedder import embed_chunks
from vectorstore import store_in_pinecone
from typing import List

pdf_path="./resources/Cir-T (7).pdf"

def run():
    pages=read_pdf(pdf_path)
    
    print(f"extracted{len(pages)}pages from the pdf.")
    print("First page content")
    print(pages[0] if pages else "No content found  ")
    
    """chunks=chunk_pages(pages,chunk_size=900, chunk_overlap=150)
    
    embedded_chunks=embed_chunks(chunks)
    print(f"Total chunks embedded:{len(embedded_chunks)}")
    print(f"first chunk embedding:{embed_chunks[0]}")
    
    store_in_pinecone(chunks,embedded_chunks)"""
    
    if __name__=="__main__":
        run()