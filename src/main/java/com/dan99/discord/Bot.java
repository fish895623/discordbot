package com.dan99.discord;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;

import com.dan99.discord.events.*;

public class Bot {
    public static void main(String[] args) throws Exception {
        JDA jda = JDABuilder.createDefault("").build();
        jda.addEventListener(new HelloEvent());
    }
}
