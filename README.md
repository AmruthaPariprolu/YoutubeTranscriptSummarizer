
# YoutubeTranscriptSummarizer

# YouTube Transcript Summarization

This  application fetches the transcript of a YouTube video using its video ID, summarizes it  and calculates the similarity between the transcript and its corresponding subtitles.
 

## Overview

This project enables users to:
- Retrieve transcripts from YouTube videos using their video IDs.
- Summarize the retrieved transcripts into concise text chunks.
- Calculate the similarity between the original transcript and formatted subtitles using cosine similarity.

## Features

- **Transcript Retrieval:** Fetches the transcript of a YouTube video.
- **Text Summarization:** Summarizes long transcripts into shorter, coherent text using the `facebook/bart-large-cnn` model.
- **Similarity Calculation:** Computes the cosine similarity between the original transcript and the subtitles, providing a similarity score.

## Usage

- Enter the YouTube video ID into the provided form on the homepage.
- Submit the form to fetch the transcript and generate the summary.
- The page will display the full transcript, the summarized version, and the similarity score between the transcript and subtitles.

