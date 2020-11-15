package com.dan99.discord;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import com.dan99.discord.events.HelloEvent;
import com.dan99.discord.events.text.createChannel;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;

public class Bot {
    public static void main(String[] args) throws Exception {

        String fileName = "token";

        File file = new File(fileName);
        FileReader fr = new FileReader(file);
        BufferedReader br = new BufferedReader(fr);
        System.out.println(br.readLine());
        br.close();
        JDA jda = JDABuilder.createDefault(br.readLine()).build();
        jda.addEventListener(new HelloEvent());
        jda.addEventListener(new createChannel());
    }
}
