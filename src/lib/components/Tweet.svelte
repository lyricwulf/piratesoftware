<script>
  import tweets from "$lib/tweets.json";
  import {
    MessageSquare,
    Repeat2,
    Heart,
    Bookmark,
    ExternalLink,
  } from "@lucide/svelte";
  import { Card } from "$lib/components/ui/card";
  import { Button } from "$lib/components/ui/button";
  const { twid, bold = [] } = $props();
  const tweet = tweets[twid];
  let tweetHtml = tweet["Tweet Text"];
  bold.forEach((word) => {
    tweetHtml = tweetHtml.replace(
      new RegExp(`(${word})`, "g"),
      `<mark>$1</mark>`
    );
  });
</script>

<Card class="p-4 flex flex-col gap-2">
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
