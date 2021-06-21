<script>
    import stringSimilarity from 'string-similarity';
    import api from '../../static/api.json';
    let data = JSON.parse(JSON.stringify(api.data));
    let view = JSON.parse(JSON.stringify(data))
    let searchTerm = '';

    let languages = {
        'c' : true,
        'lua' : true,
        'python' : true,
        'eel' : true,
    }

    async function updateSearch() {
        if (searchTerm === '') {
            view = JSON.parse(JSON.stringify(api.data));
        } else {
            data.forEach(d => {
                d.dist = stringSimilarity.compareTwoStrings(searchTerm.toLowerCase(), d.name.toLowerCase())
            })
            
            data.sort((a, b) => a.dist - b.dist)
            view = data.reverse().slice(0, 10)
        }
    }
    
</script>

<div class='search'>
    <input type=text id='search-input' placeholder='Search the Reascript API' bind:value={searchTerm} on:input={updateSearch} />
    <div class='language-toggles'>
        <label>
            <input type=checkbox bind:checked={languages.c}> 
            <span>C</span>
        </label>
        <label>
            <input type=checkbox bind:checked={languages.lua}> 
            <span>Lua</span>
        </label>
        <label>
            <input type=checkbox bind:checked={languages.python}> 
            <span>Python</span>
        </label>
        <label>
            <input type=checkbox bind:checked={languages.eel}> 
            <span>EEL2</span>
        </label>
    </div>
</div>

<div class='container'>
    {#each view as f}
        <div class='function'>
            <hr>
            <div class='function-name' class:exact={f.dist >= 0.75}>{f.name}</div>
            {#if f.langs.c_func && languages.c}
            <span class='code'>{@html f.langs.c_func}</span>
            {/if}

            {#if f.langs.l_func && languages.lua}
            <span class='code'>{@html f.langs.l_func}</span>
            {/if}

            {#if f.langs.p_func && languages.python}
            <span class='code'>{@html f.langs.p_func}</span>
            {/if}

            {#if f.langs.e_func && languages.eel}
            <span class='code'>{@html f.langs.e_func}</span>
            {/if}
        </div>
    {/each}
</div>

<style>
    .container {
        max-width: 1400px;
        margin: 0 auto;
    }

    .function {
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .function-name {
        font-weight: bold;
        font-size: 1.5em;
        padding-bottom: 15px;
    }

    .search {
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }

    .language-toggles {
        margin-top: 20px;
        margin-bottom: 20px;
        display: flex;
        flex-direction: row;
        gap: 20px;

    }

    #search-input {
        font-size: 36px;
        text-align: center;
        max-width: 50%;;
    }

    .exact {
        color: rgb(0, 102, 255);
        font-style: italic;
    }

    label {
        align-content: center;
    }
</style>

