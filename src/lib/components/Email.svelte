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
  import Button from "$lib/components/ui/button/button.svelte";
  import { ChevronDown, Download } from "@lucide/svelte";

  const { eml, open: openProp } = $props();

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

  let open = $state(openProp ?? true);
</script>

<div class="email flex flex-col w-full rounded-lg overflow-hidden">
  {#if email}
    <div class="email-banner bg-gray-900 flex flex-row items-center p-4 gap-2">
      <svg
        width="100%"
        height="100%"
        viewBox="0 0 100 100"
        class="absolute left-0 top-0 w-full h-full opacity-10"
        preserveAspectRatio="none"
      >
        <polygon
          points="0,100 100,100 50,20"
          stroke="grey"
          fill="none"
          stroke-width="1"
          stroke-linejoin="round"
        />
        <polygon
          points="0,0 100,0 50,80"
          stroke="white"
          fill="none"
          stroke-width="1"
          stroke-linejoin="round"
        />
      </svg>
      <div class="flex flex-col w-full h-fit items-start z-1">
        <span class="shrink-0 font-bold bg-gray-900">{email.subject}</span>
        <span class="text-sm text-gray-400 bg-gray-900">
          {email.date
            ? new Date(email.date).toLocaleString("en-US", {
                dateStyle: "long",
                timeStyle: "short",
                timeZone: "PST",
              })
            : ""}
        </span>
        <span class="text-sm flex flex-row gap-2 bg-gray-900">
          {#each iter(email.from) as from}
            <Tooltip.Root openDelay={100}>
              <Tooltip.Trigger class="hover:bg-gray-200/20">
                {from.name || from.email}
              </Tooltip.Trigger>
              <Tooltip.Content
                class="bg-popover text-popover-foreground softborder"
              >
                <p>{from.email}</p>
              </Tooltip.Content>
            </Tooltip.Root>
          {/each}
          <span> -> </span>
          {#each iter(email.to) as to}
            <Tooltip.Root openDelay={100}>
              <Tooltip.Trigger class="hover:bg-gray-200/20">
                {to.name || to.email}
              </Tooltip.Trigger>
              <Tooltip.Content
                class="bg-popover text-popover-foreground softborder"
              >
                <p>{to.email}</p>
              </Tooltip.Content>
            </Tooltip.Root>
          {/each}
        </span>
      </div>
      <div>
        <span class="text-sm flex flex-col">
          <Tooltip.Root openDelay={100}>
            <Tooltip.Trigger>
              <Button href={emailUrl} variant="ghost" size="icon">
                <Download />
              </Button>
            </Tooltip.Trigger>
            <Tooltip.Content
              class="bg-popover text-popover-foreground softborder"
            >
              <p>Download as .eml</p>
            </Tooltip.Content>
          </Tooltip.Root>

          <Button onclick={() => (open = !open)} variant="ghost" size="icon">
            <span
              class="transition"
              class:rotate-360={!open}
              class:rotate-180={open}
            >
              <ChevronDown />
            </span>
          </Button>
        </span>
      </div>
    </div>
    {#if email.html}
      <iframe
        class="collapsible w-full h-96 bg-white"
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

  .email-banner {
    position: relative;
  }
  /* .email-banner::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 1000px;
    height: 1000px;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: inherit;
    z-index: 1;
    transform: rotate(45deg) translate(calc(-500px - 50%), -500px);
  } */
</style>
