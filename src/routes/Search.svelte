<script lang="ts">
  import { prepareSearchData, searchRefs, type SearchResults } from "./search";
  import { Card } from "$lib/components/ui/card";
  import { untrack } from "svelte";
  import { Search, X } from "@lucide/svelte";
  import { onNavigate } from "$app/navigation";
  import Button from "$lib/components/ui/button/button.svelte";

  let results: SearchResults = $state([]);

  let searchQuery = $state("");
  let searchState = $state({
    query: "",
    loading: false,
    t: undefined as ReturnType<typeof setTimeout> | undefined,
  });

  let open = $state(false);

  let inputElement: HTMLInputElement | undefined = $state();

  searchRefs.openSearch = () => {
    resetSearch();
    open = true;
    function focusInput() {
      requestAnimationFrame(() => {
        if (inputElement) {
          inputElement.focus();
        } else {
          focusInput();
        }
      });
    }

    focusInput();
  };

  $effect(() => {
    void searchQuery;
    untrack(() => {
      clearTimeout(searchState.t);

      if (!searchQuery) {
        results = [];
      } else {
        searchState.query = searchQuery;
        searchState.loading = true;
      }
    });

    (async () => {
      const index = await prepareSearchData();
      const query = searchQuery; // important: Capture the current query
      if (!query) {
        results = [];
        searchState.loading = false;
        return;
      }
      await new Promise(
        (resolve) => (searchState.t = setTimeout(resolve, 500))
      );
      // wait for animation end
      const loaderElement = document.querySelector(
        ".can-load"
      ) as HTMLLabelElement;
      if (loaderElement)
        await new Promise((resolve) => {
          loaderElement.addEventListener("animationiteration", resolve, {
            once: true,
          });
        });

      if (searchQuery !== query) return;

      results = index.search(query, {
        pluck: "text",
        enrich: true,
        highlight: {
          template: "<b>$1</b>",
          boundary: 600,
          merge: true,
        },
        suggest: true,
      }) as SearchResults;

      searchState.loading = false;
    })();
  });

  function closeSearch() {
    open = false;
  }

  function resetSearch() {
    searchQuery = "";
    results = [];
  }

  onNavigate(closeSearch);
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
      class="w-[calc(100vw-2rem)] max-w-200 bg-background rounded-xl border-1 p-4 flex
  flex-col overflow-clip"
    >
      <div class="flex gap-2 items-center">
        <label
          class="grow-1 w-0 can-load py-2 px-4 flex items-center gap-2 rounded-full border-1 border-gray-600"
          class:loading={searchState.loading}
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
        <Button
          class="grow-0 shrink-0 w-12 h-12 rounded-full text-muted-foreground"
          variant="outline"
          size="sm"
          onclick={closeSearch}
        >
          <X size="24" />
        </Button>
      </div>
      {#if searchState.loading}{:else}
        {#if searchQuery}
          <div class="result-count text-sm text-muted-foreground my-2">
            {results?.length > 0
              ? `${results.length} result${results.length > 1 ? "s" : ""} found for "${searchQuery}"`
              : `${searchQuery ? `No results found for "${searchQuery}"` : ""}`}
          </div>
        {/if}

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
        {/if}
      {/if}
    </div>
  </div>
{/if}

<style>
  .result-preview {
    max-height: 100px;
    overflow: hidden;
  }

  .result-preview :global(b) {
    color: hsl(var(--foreground));
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

  .can-load {
    transition: box-shadow 0.3s var(--ease-out);
    box-shadow: 0 0 0px var(--color-blue-500);
  }

  .loading {
    animation: skeleton 0.6s infinite var(--ease-out);
  }

  @keyframes skeleton {
    0% {
      box-shadow: 0 0 0px var(--color-blue-500);
    }
    50% {
      box-shadow: 0 0 20px var(--color-blue-500);
    }
    0% {
      box-shadow: 0 0 0px var(--color-blue-500);
    }
  }
</style>
