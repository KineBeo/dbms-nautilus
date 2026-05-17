# BC004: float_cast_overflow_in_alsoAnInt

**Severity:** LOW
**Subtype:** float-cast-overflow
**Key function:** `alsoAnInt`
**CVE:** none
**Versions affected:** 3.30.1, 3.31.1, 3.32.0, 3.32.2
**Total crash count:** 132
**Unique hashes:** 56

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:84141:16: runtime error: 1.11111e+21 is outside the range of representable values of type 'long long'
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:84141:16: runtime error: 1.11111e+21 is outside the range of representable values of type 'long long'
alsoAnInt
applyNumericAffinity
applyAffinity
sqlite3VdbeExec
```

## Crash hashes

- `22e03ff823a91eeb`
- `51834f9aa4aa5764`
- `139f9b760acdec6c`
- `ea651014c68a8c63`
- `8063d7f2dab3aa47`
- `af42fbc90328ea1b`
- `9b417ddb2441b15c`
- `ecb096e874db4127`
- `f47936504b6ce4f8`
- `7a150746873bd972`
- `aadcf1b2dcda72cb`
- `be86f789855f370c`
- `f6519b84ed0086f5`
- `5c094ac1f74c70d7`
- `d6e644ab4f02b621`
- `b092512c678427bf`
- `262e18785d939f8a`
- `82e98781d9c0c32b`
- `69b29031fffd6ba2`
- `3412d5e813f34af2`
- `e1a8b2c4a5592093`
- `9f731f26f91fb417`
- `6767d03e8a9312b4`
- `59acd7889b3fa6d8`
- `9c78515a92aa839a`
- `85d980a95b84570b`
- `c7c06fb639370535`
- `643205a858474f64`
- `3e9719a6638492ac`
- `c0c113d15a713f84`
- `f959748d4f4b6301`
- `a44a8765ca6148ae`
- `6014f3d156178710`
- `6ac041ad7583ecf6`
- `cfa8c34bdbc017db`
- `162f3109adc65df2`
- `81b86882c247e0c3`
- `b2fe4ab7b1064eb4`
- `7a136f84a686af06`
- `b9c2638dab5a5a63`
- `3cac9102ffb376dc`
- `2904e1f2a166c6f0`
- `2d23c9af326c2626`
- `1dfbd00b4e94e6f1`
- `b5206ee5283a9260`
- `77380288837142c8`
- `082d290a01ade500`
- `e4da1461ccf620ab`
- `db1c6705639ceda6`
- `6cc400f1164c2563`
- `0aa73e46fc9d0361`
- `0f7b4b560bea87a3`
- `195015b3846edaa1`
- `387b874505511dee`
- `11592883476d3cf5`
- `33132ed9e6853c32`
