


                     ┌─────────────────────────┐
                     │      Streamlit App      │
                     │ (User Upload + Query)   │
                     └─────────────┬───────────┘
                                   │
───────────────────────────────────┼────────────────────────────────────────
                                   │
                    FILE UPLOAD FLOW (load_only = False)
───────────────────────────────────┼────────────────────────────────────────
                                   ▼

                        User Uploads a File
                   (PDF / DOCX / TXT in Streamlit)

                                   │
                                   ▼

                       create_or_update_chroma_db
                           (file_path, load_only=False)
                                   │
                                   ▼

                     ┌──────────────────────────┐
                     │   load_document()        │
                     │ Extract text from file   │
                     └─────────────┬────────────┘
                                   ▼

                     ┌──────────────────────────┐
                     │      chunk_text()        │
                     │ Split text into chunks   │
                     └─────────────┬────────────┘
                                   ▼

                     ┌──────────────────────────┐
                     │ CohereEmbeddings         │
                     │ Generate embeddings      │
                     └─────────────┬────────────┘
                                   ▼

                     ┌──────────────────────────┐
                     │  Chroma DB (persisted)   │
                     │ Add new embeddings       │
                     └─────────────┬────────────┘
                                   ▼

                         Embeddings saved permanently
                 New knowledge is now added to Chroma DB

───────────────────────────────────┼────────────────────────────────────────
                                   │
                       QUESTION FLOW (load_only = True)
───────────────────────────────────┼────────────────────────────────────────
                                   ▼

                   User Asks a Question in Streamlit

                                   │
                                   ▼

                    create_or_update_chroma_db(load_only=True)
                      → Only load existing Chroma DB
                      → NO embedding computation
                      → NO expensive Cohere calls
                      → Very fast

                                   │
                                   ▼

                     vectordb.as_retriever(k=3).invoke()
                      → Find best matching context chunks

                                   │
                                   ▼

                     prompt_reader(context, question)
                      → Build clean final prompt

                                   │
                                   ▼

                     Groq LLM (ChatGroq) generates answer

                                   │
                                   ▼

                        Answer displayed in Streamlit
