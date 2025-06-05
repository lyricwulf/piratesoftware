<script lang="ts">
  import { prepareSearchData, searchRefs, type SearchResults } from "./search";
  import { Card } from "$lib/components/ui/card";
  import { untrack } from "svelte";
  import { Search } from "@lucide/svelte";

  let results: SearchResults = $state([]);

  let searchQuery = $state("Thor");

  let open = $state(false);

  let inputElement: HTMLInputElement | undefined = $state();

  searchRefs.openSearch = () => {
    open = true;
    searchQuery = "";
    results = [];
    requestAnimationFrame(() => {
      inputElement?.focus();
    });
  };

  $effect(() => {
    if (!searchQuery) {
      untrack(() => {
        results = [];
      });
    }
    (async () => {
      const index = await prepareSearchData();
      if (searchQuery) {
        results = index.search(searchQuery, {
          pluck: "text",
          enrich: true,
          highlight: {
            template: "<b>$1</b>",
            boundary: 600,
            merge: true,
          },
          suggest: true,
        }) as SearchResults;
      } else {
        results = [];
      }
    })();
  });
</script>

{#if open}
  <div
    class="fixed inset-0 z-40 bg-black/50"
    onclick={(e) => (open = false)}
    onkeypress={(e) => {
      if (e.key === "Escape") {
        open = false;
      }
    }}
    role="button"
    tabindex="0"
  ></div>

  <div
    class="search-wrapper fixed mb-4 top-0 left-0 right-0 z-50 flex flex-col
  items-center p-4 shadow-md"
    onclick={(e) => e.target === e.currentTarget && (open = false)}
    onkeypress={(e) => {
      if (e.key === "Escape") {
        open = false;
      }
    }}
    role="button"
    tabindex="0"
  >
    <div
      class="w-[calc(100vw-2rem)] max-w-200 bg-background rounded-xl border-1 p-4 pb-0 flex
  flex-col overflow-clip"
    >
      <label
        class="py-2 px-4 flex items-center gap-2 rounded-lg border-1 border-gray-600"
      >
        <Search class="grow-0 shrink-0" size={20} />
        <input
          class="text-xl grow-1 basis-0"
          type="text"
          placeholder="Search..."
          bind:value={searchQuery}
          bind:this={inputElement}
        />
      </label>

      <div class="result-count text-sm text-muted-foreground my-2">
        {results?.length > 0
          ? `${results.length} result${results.length > 1 ? "s" : ""} found for "${searchQuery}"`
          : `${searchQuery ? `No results found for "${searchQuery}"` : ""}`}
      </div>

      {#if results?.length > 0}
        <div class="h-[80vh] overflow-y-auto results">
          <ul>
            {#each results as { highlight, doc: { text, routeStr, title } }}
              <li>
                <Card class="mb-4 p-4">
                  <div class="text-lg text-primary font-semibold mb-1">
                    <a href={routeStr}>{title}</a>
                  </div>
                  <div
                    class="result-preview text-sm text-muted-foreground font-normal"
                  >
                    {@html highlight}
                  </div>
                </Card>
              </li>
            {/each}
          </ul>
        </div>
      {:else}{/if}
    </div>
  </div>
{/if}

<style>
  .result-preview {
    max-height: 100px;
    overflow: hidden;
  }

  .result-preview :global(b) {
    /* color: hsl(var(--foreground)); */
    font-weight: bold;
  }

  .results {
    margin-right: -1rem;
    scrollbar-gutter: stable;
    padding-right: 1rem;
  }

  input:focus {
    outline: none;
  }

  label {
    transition:
      color 0.3s var(--ease-out-expo),
      border-color 0.3s var(--ease-out-expo);
  }

  label:not(:focus-within) {
    color: hsl(var(--muted-foreground));
    border-color: hsl(var(--border));
  }
</style>
