<script lang="ts">
  import tweets from "$lib/tweets.json";
  import {
    MessageSquare,
    Repeat2,
    Heart,
    Bookmark,
    ExternalLink,
    Link,
  } from "@lucide/svelte";
  import { Card } from "$lib/components/ui/card";
  import { Button } from "$lib/components/ui/button";

  interface TweetProps {
    twid: keyof typeof tweets;
    bold?: string[];
  }

  const { twid, bold = [] }: TweetProps = $props();
  const tweet = $derived(tweets[twid]);
  let tweetHtml = $derived(
    (() => {
      let text = tweet["Tweet Text"];
      bold.forEach((word) => {
        text = text.replace(new RegExp(`(${word})`, "g"), `<mark>$1</mark>`);
      });
      text = text.replace(/^(@\w+ )+/g, (match) => {
        return `<span class="font-light text-xs text-muted-foreground">Replying to ${match}</span><br />`;
      });
      text = text.replaceAll(/\@([a-zA-Z0-9_]+)/g, (match) => {
        return `<a href="https://twitter.com/${match.slice(1)}" target="_blank" rel="external">${match}</a>`;
      });
      return text;
    })()
  );
</script>

<Card class="p-4 flex flex-col gap-2" id={`tweet-${twid}`}>
  <div class="flex justify-between items-start">
    <div class="flex flex-col">
      <span class="font-bold">{tweet["Author Name"]}</span>
      <span class="text-sm text-muted-foreground">
        <a
          href="https://twitter.com/{tweet['Author Username']}"
          rel="external"
          target="_blank"
        >
          @{tweet["Author Username"]}
        </a>
      </span>
    </div>
    <Button
      variant="ghost"
      href={`#tweet-${twid}`}
      class="text-muted-foreground"
    >
      <Link size="20" />
    </Button>
  </div>
  <div>
    {@html tweetHtml}
  </div>
  <div>
    <span class="text-sm text-muted-foreground">{tweet["Creation Time"]}</span>
  </div>
  <div class="flex justify-between text-muted-foreground max-w-100">
    <div class="flex gap-1 items-center text-sm">
      <MessageSquare size="20" /><span>{tweet["Reply Count"]}</span>
    </div>
    <div class="flex gap-1 items-center text-sm">
      <Repeat2 size="22" /><span>{tweet["Retweet Count"]}</span>
    </div>
    <div class="flex gap-1 items-center text-sm">
      <Heart size="20" /><span>{tweet["Like Count"]}</span>
    </div>
    <div class="flex gap-1 items-center text-sm">
      <Bookmark size="20" /><span>{tweet["Bookmark Count"]}</span>
    </div>
    <div class="flex gap-1 items-center text-sm">
      <Button variant="ghost" href={tweet["Tweet URL"]} target="_blank">
        <ExternalLink size="20" />
      </Button>
    </div>
  </div>
</Card>
