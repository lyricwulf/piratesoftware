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
  import { iter } from "$lib/util/iter";
  import * as Tooltip from "$lib/components/ui/tooltip";
  import { ChevronDown } from "@lucide/svelte";

  const { eml } = $props();

  const pathname = page.url.pathname;
  const emailUrl = `${pathname}/${eml}`;

  let email = $state<ReadedEmlJson>();
  onMount(() => {
    (async () => {
      const response = await fetch(emailUrl);
      const blob = await response.text();
      const result = readEml(blob);
      if (typeof result === "string") {
        console.error("Error parsing EML:", result);
        return;
      }
      if (result instanceof Error) {
        console.error("Error parsing EML:", result);
        return;
      }
      email = result;
      console.log(email);
    })();
  });

  let open = $state(true);
</script>

<div
  class="email flex flex-col gap-1 w-full bg-gray-800 rounded-lg overflow-hidden"
>
  {#if email}
    <div class="flex flex-col w-full h-fit p-4 items-start">
      <span class="shrink-0 font-bold">{email.subject}</span>
      <span class="text-sm text-gray-400">
        {email.date
          ? new Date(email.date).toLocaleString("en-US", {
              dateStyle: "long",
              timeStyle: "short",
              timeZone: "PST",
            })
          : ""}
      </span>
      <span class="text-sm flex flex-row gap-2">
        {#each iter(email.from) as from}
          <Tooltip.Root openDelay={100}>
            <Tooltip.Trigger class="hover:bg-gray-200/20">
              {from.name}
            </Tooltip.Trigger>
            <Tooltip.Content
              class="bg-popover text-popover-foreground softborder"
            >
              <p>{from.email}</p>
            </Tooltip.Content>
          </Tooltip.Root>
        {/each}
        <span> -> </span>
        {#each iter(email.to) as from}
          <Tooltip.Root openDelay={100}>
            <Tooltip.Trigger class="hover:bg-gray-200/20">
              {from.name}
            </Tooltip.Trigger>
            <Tooltip.Content
              class="bg-popover text-popover-foreground softborder"
            >
              <p>{from.email}</p>
            </Tooltip.Content>
          </Tooltip.Root>
        {/each}
      </span>
      <span class="text-sm flex flex-row justify-between w-full">
        <span></span>
        <button
          onclick={() => (open = !open)}
          class="transition"
          class:rotate-360={!open}
          class:rotate-180={open}
        >
          <ChevronDown />
        </button>
        <a href={emailUrl}>Download as .eml</a>
      </span>
    </div>
    {#if email.html}
      <iframe
        class="collapsible w-full h-96 bg-gray-200"
        title={email.headers.Subject}
        srcdoc={email.html}
        class:open
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

  .collapsible {
    transition: all 0.3s var(--ease-out-expo);
    overflow: hidden;
  }
  .collapsible:not(.open) {
    height: 0;
  }
</style>
