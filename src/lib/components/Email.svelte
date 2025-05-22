<script lang="ts">
  import { onMount } from "svelte";
  import {
    parseEml,
    readEml,
    GBKUTF8,
    decode,
    type ReadedEmlJson,
  } from "eml-parse-js";
  import { page } from "$app/state";
  import KvTable from "$lib/components/KvTable.svelte";
  import * as Collapsible from "$lib/components/ui/collapsible";
  import Button from "$lib/components/ui/button/button.svelte";
  import { iter } from "$lib/util/iter";

  const { eml } = $props();

  const pathname = page.url.pathname;
  const emailUrl = `${pathname}/${eml}`;

  let email = $state<ReadedEmlJson>();
  onMount(() => {
    (async () => {
      const response = await fetch(emailUrl);
      const blob = await response.text();
      email = readEml(blob);
      console.log(email);
    })();
  });
</script>

<div
  class="email flex flex-col gap-1 w-full bg-gray-800 rounded-lg overflow-hidden"
>
  {#if email}
    <div class="flex flex-col w-full h-fit p-4">
      <span class="shrink-0 font-bold">{email.headers.Subject}</span>
      <span class="text-sm text-gray-400">
        {email.date
          ? new Date(email.date).toLocaleString("en-US", {
              dateStyle: "long",
              timeStyle: "short",
              timeZone: "PST",
            })
          : ""}
      </span>
      <span class="text-sm">
        {iter(email.from).map((o) => o.email)}
        ->
        {iter(email.to).map((o) => o.email)}
      </span>
      <a href={emailUrl} class="text-sm"> Download as .eml </a>
    </div>
    {#if email.html}
      <iframe
        class="w-full h-96 bg-gray-200"
        title={email.headers.Subject}
        srcdoc={email.html}
      >
      </iframe>
    {/if}
  {:else}
    <div>Loading...</div>
  {/if}
</div>

<style>
  .email {
    box-shadow: 0 0 2px 0 rgba(255, 255, 255, 1);
  }
</style>
