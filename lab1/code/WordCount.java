//package org.myorg;
import java.io.IOException;
import java.util.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class WordCount {
    public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();
        private String currentString = new String("");
        public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
            String line = value.toString();
            StringTokenizer tokenizer = new StringTokenizer(line);
            while (tokenizer.hasMoreTokens()) {
                currentString = tokenizer.nextToken();
                currentString = this.decapitalize(currentString);
                word.set(this.firstCharacterise(currentString));
                output.collect(word, one);
            }
        }
        public String decapitalize(String string){
            if (string == null || string.length() == 0) {
                return string;
            }
            char c[] = string.toCharArray();
            char firstCharacter = c[0];
            if (Character.isLetter(firstCharacter)){
                c[0] = Character.toLowerCase(firstCharacter);
            }
            return new String(c);
        }

        public String firstCharacterise(String string){
            if (string == null || string.length() == 0) {
                return string;
            }
            char c[] = string.toCharArray();
            char firstCharacter = c[0];
            return new String(firstCharacter);
        }
    }
	
    public static class Reduce extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable> {
        public void reduce(Text key, Iterator<IntWritable> values, OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException {
            int sum = 0;
            while (values.hasNext()) {
                sum += values.next().get();
            }
            output.collect(key, new IntWritable(sum));
        }
    }
	
    public static void main(String[] args) throws Exception {
        JobConf conf = new JobConf(WordCount.class);
        conf.setJobName("wordcount");
	    
        conf.setOutputKeyClass(Text.class);
        conf.setOutputValueClass(IntWritable.class);
	    
        conf.setMapperClass(Map.class);
        conf.setReducerClass(Reduce.class);
	    
        conf.setInputFormat(TextInputFormat.class);
        conf.setOutputFormat(TextOutputFormat.class);
	    
        FileInputFormat.setInputPaths(conf, new Path(args[0]));
        FileOutputFormat.setOutputPath(conf, new Path(args[1]));
	    
        JobClient.runJob(conf);
    }
}
