from __future__ import absolute_import
import argparse
import re
import csv
import os
import logging
import apache_beam as beam

from apache_beam.options.pipeline_options import PipelineOptions,GoogleCloudOptions,StandardOptions
from apache_beam.io import BigQuerySource

class Dataingestion():
    def parse_method(self,strinput):
        
        row = dict(zip(('id','name','date','user_id','class','tag_based'),strinput))
        
        return row


def run(argv= None):

    parser = argparse.ArgumentParser()
   

    parser.add_argument('--input', dest='input',required=False,help='Input file is read from local or',default= 'gs://mydstore/result1.csv')


    parser.add_argument('--output', dest= 'output', required=False, help='output BQ table to write results to',default='emp.empdata')


    known_args, pipeline_args = parser.parse_known_args(argv)

    dataingestion = Dataingestion()
    
    options=PipelineOptions(pipeline_args)
    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.job_name = 'myjob'
    google_cloud_options.staging_location = 'gs://mydstore/result1.csv'
    google_cloud_options.temp_location = 'gs://mydstore/temp'
    p = beam.Pipeline(options= options)
    
    (p
    |'Read from a file' >> beam.io.ReadFromText(known_args.input, skip_header_lines=1)

    |'String to BigQuery Row' >> beam.Map(lambda s: dataingestion.parse_method(s))

    |'Write to Bigquery' >> beam.io.Write(beam.io.WriteToBigQuery(known_args.output , schema= 'id : STRING,name : STRING,date : STRING, user_id : STRING,class : STRING,tag_based : STRING',
    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
    write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)))
    p.run().wait_until_finish()

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    run()
