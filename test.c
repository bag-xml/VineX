//----- (00060868) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController .cxx_destruct](VNActivityTableViewController *self, SEL a2)
{
  objc_storeStrong((id *)&self->_endpoint, 0);
  objc_storeStrong((id *)&self->_loaderView, 0);
  objc_storeStrong((id *)&self->_anchor, 0);
  objc_storeStrong((id *)&self->_urls, 0);
  objc_storeStrong((id *)&self->_attributedStrings, 0);
  objc_storeStrong((id *)&self->_feed, 0);
  j__objc_storeStrong((id *)&self->_dateFormatter, 0);
}

//----- (00060848) --------------------------------------------------------
char __cdecl -[VNActivityTableViewController activityRequestComplete](VNActivityTableViewController *self, SEL a2)
{
  return self->_activityRequestComplete;
}

//----- (00060858) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController setActivityRequestComplete:](
        VNActivityTableViewController *self,
        SEL a2,
        char a3)
{
  self->_activityRequestComplete = a3;
}

//----- (00060820) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController setEndpoint:](VNActivityTableViewController *self, SEL a2, id a3)
{
  NSString *v4; // r0
  NSString *endpoint; // r1

  v4 = (NSString *)objc_retain(a3);
  endpoint = self->_endpoint;
  self->_endpoint = v4;
  j__objc_release(endpoint);
}

//----- (0006078C) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController reload](VNActivityTableViewController *self, SEL a2)
{
  -[VNActivityTableViewController load:size:addToExistingResults:](self, "load:size:addToExistingResults:", -1, -1, 0);
}

//----- (000607B4) --------------------------------------------------------
char __cdecl -[VNActivityTableViewController isEmpty](VNActivityTableViewController *self, SEL a2)
{
  NSMutableArray *feed; // r0
  id v4; // r1
  char result; // r0

  feed = self->_feed;
  if ( !feed )
    return (unsigned __int8)objc_msgSend(self->_loaderView, "isAnimating") == 0;
  v4 = objc_msgSend(feed, "count");
  result = 0;
  if ( !v4 )
    return (unsigned __int8)objc_msgSend(self->_loaderView, "isAnimating") == 0;
  return result;
}

//----- (00060810) --------------------------------------------------------
NSString *__cdecl -[VNActivityTableViewController endpoint](VNActivityTableViewController *self, SEL a2)
{
  return self->_endpoint;
}

//----- (0006022C) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController load:size:addToExistingResults:](
        VNActivityTableViewController *self,
        SEL a2,
        unsigned int a3,
        unsigned int a4,
        char a5)
{
  NSString *v8; // r0
  bool v9; // zf
  NSString *v10; // r10
  id v11; // r0
  NSString *v12; // r6
  VNAPIManager *v13; // r0
  VNAPIManager *v14; // r8
  int v15[5]; // [sp+10h] [bp-64h] BYREF
  id v16; // [sp+24h] [bp-50h]
  int v17[5]; // [sp+28h] [bp-4Ch] BYREF
  id v18; // [sp+3Ch] [bp-38h]
  int v19[5]; // [sp+40h] [bp-34h] BYREF
  id v20; // [sp+54h] [bp-20h]
  char v21; // [sp+58h] [bp-1Ch]

  v8 = objc_retain(self->_endpoint);
  v9 = a3 == -1;
  v10 = v8;
  if ( a3 != -1 )
    v9 = a4 == -1;
  if ( !v9 )
  {
    v11 = objc_msgSend(v8, "stringByAppendingFormat:", CFSTR("?page=%i&size=%i&anchor=%@"), a3, a4, self->_anchor);
    v12 = (NSString *)objc_retainAutoreleasedReturnValue(v11);
    objc_release(v10);
    v10 = v12;
  }
  v13 = +[VNAPIManager sharedInstance](&OBJC_CLASS___VNAPIManager, "sharedInstance");
  v14 = objc_retainAutoreleasedReturnValue(v13);
  v19[0] = (int)_NSConcreteStackBlock;
  v19[1] = 1107296256;
  v19[2] = 0;
  v19[3] = (int)sub_603A4;
  v19[4] = (int)&unk_415B10;
  v20 = objc_retain(self);
  v17[0] = (int)_NSConcreteStackBlock;
  v17[1] = 1107296256;
  v17[2] = 0;
  v17[3] = (int)sub_6071C;
  v21 = a5;
  v17[4] = (int)&unk_415B30;
  v15[0] = (int)_NSConcreteStackBlock;
  v15[1] = 1107296256;
  v15[2] = 0;
  v15[3] = (int)sub_60754;
  v18 = objc_retain(v20);
  v15[4] = (int)&unk_415B50;
  v16 = objc_retain(v18);
  -[VNAPIManager request:endpoint:parameters:success:error:failed:](
    v14,
    "request:endpoint:parameters:success:error:failed:",
    CFSTR("GET"),
    v10,
    0,
    v19,
    v17,
    v15);
  objc_release(v14);
  objc_release(v16);
  objc_release(v18);
  objc_release(v20);
  objc_release(v10);
}
// 603A4: using guessed type int __fastcall sub_603A4(int, id);
// 6071C: using guessed type int sub_6071C();
// 60754: using guessed type int sub_60754();
// 3E921C: using guessed type __objc2_class OBJC_CLASS___VNAPIManager;
// 3FB648: using guessed type __CFString cfstr_PageISizeIAnch;
// 3FB658: using guessed type __CFString cfstr_Get;

//----- (000603A4) --------------------------------------------------------
void __fastcall sub_603A4(int a1, void *a2)
{
  id v3; // r5
  id v4; // r0
  id v5; // r4
  id v6; // r0
  id v7; // r6
  int v8; // r1
  id v9; // r0
  id v10; // r6
  id v11; // r0
  id v12; // r6
  id v13; // r0
  id v14; // r0
  int v15; // r3
  void *v16; // r1
  void *v17; // r11
  void *v18; // r4
  id v19; // r0
  id v20; // r6
  id v21; // r0
  id v22; // r4
  id v23; // r0
  int v24; // r2
  void *v25; // r1
  void *v26; // r0
  id v27; // r0
  id v28; // r0
  int v29; // r3
  void *v30; // r1
  void *v31; // r10
  id v32; // r0
  id v33; // r4
  id v34; // r0
  id v35; // r6
  UIAccessibilityNotifications v36; // r10
  id v37; // r0
  id v38; // r5
  id v39; // r0
  id v40; // r4
  id v41; // r0
  id v42; // r6

  v3 = objc_retain(a2);
  *(_BYTE *)(*(_DWORD *)(a1 + 20) + 272) = 1;
  v4 = objc_msgSend(v3, "objectForKey:", CFSTR("nextPage"));
  v5 = objc_retainAutoreleasedReturnValue(v4);
  v6 = objc_msgSend(&OBJC_CLASS___NSNull, "null");
  v7 = objc_retainAutoreleasedReturnValue(v6);
  objc_release(v7);
  objc_release(v5);
  v8 = *(_DWORD *)(a1 + 20);
  if ( v5 == v7 )
  {
    *(_BYTE *)(v8 + 244) = 0;
  }
  else
  {
    *(_BYTE *)(v8 + 244) = 1;
    v9 = objc_msgSend(v3, "objectForKey:", CFSTR("nextPage"));
    v10 = objc_retainAutoreleasedReturnValue(v9);
    *(_DWORD *)(*(_DWORD *)(a1 + 20) + 248) = objc_msgSend(v10, "intValue");
    objc_release(v10);
    v11 = objc_msgSend(v3, "objectForKey:", CFSTR("size"));
    v12 = objc_retainAutoreleasedReturnValue(v11);
    *(_DWORD *)(*(_DWORD *)(a1 + 20) + 252) = objc_msgSend(v12, "intValue");
    objc_release(v12);
    v13 = objc_msgSend(v3, "objectForKey:", CFSTR("anchor"));
    v14 = objc_retainAutoreleasedReturnValue(v13);
    v15 = *(_DWORD *)(a1 + 20);
    v16 = *(void **)(v15 + 256);
    *(_DWORD *)(v15 + 256) = v14;
    objc_release(v16);
  }
  v17 = v3;
  if ( *(_BYTE *)(a1 + 24) )
  {
    v18 = *(void **)(*(_DWORD *)(a1 + 20) + 232);
    v19 = objc_msgSend(v3, "objectForKey:", CFSTR("records"));
    v20 = objc_retainAutoreleasedReturnValue(v19);
    v21 = objc_msgSend(v18, "arrayByAddingObjectsFromArray:", v20);
    v22 = objc_retainAutoreleasedReturnValue(v21);
    v23 = objc_msgSend(v22, "mutableCopy");
    v24 = *(_DWORD *)(a1 + 20);
    v25 = *(void **)(v24 + 232);
    *(_DWORD *)(v24 + 232) = v23;
    objc_release(v25);
    objc_release(v22);
    v26 = v20;
  }
  else
  {
    v27 = objc_msgSend(v3, "objectForKey:", CFSTR("records"));
    v28 = objc_retainAutoreleasedReturnValue(v27);
    v29 = *(_DWORD *)(a1 + 20);
    v30 = *(void **)(v29 + 232);
    *(_DWORD *)(v29 + 232) = v28;
    v26 = v30;
  }
  objc_release(v26);
  if ( !objc_msgSend(*(id *)(*(_DWORD *)(a1 + 20) + 232), "count") )
  {
    v31 = *(void **)(a1 + 20);
    v32 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
    v33 = objc_retainAutoreleasedReturnValue(v32);
    v34 = objc_msgSend(v33, "localizedStringForKey:value:table:", CFSTR("ActivityEmptyCell"), &stru_3FADD8, 0);
    v35 = objc_retainAutoreleasedReturnValue(v34);
    objc_msgSend(v31, "setEmptyCellText:", v35);
    objc_release(v35);
    objc_release(v33);
  }
  objc_msgSend(*(id *)(a1 + 20), "rebuildMeta");
  objc_msgSend(*(id *)(a1 + 20), "stopLoading");
  if ( !*(_BYTE *)(a1 + 24) )
  {
    v36 = UIAccessibilityScreenChangedNotification;
    v37 = objc_msgSend(*(id *)(a1 + 20), "tableView");
    v38 = objc_retainAutoreleasedReturnValue(v37);
    v39 = objc_msgSend(&OBJC_CLASS___NSIndexPath, "indexPathForRow:inSection:", 0, 0);
    v40 = objc_retainAutoreleasedReturnValue(v39);
    v41 = objc_msgSend(v38, "cellForRowAtIndexPath:", v40);
    v42 = objc_retainAutoreleasedReturnValue(v41);
    UIAccessibilityPostNotification(v36, v42);
    objc_release(v42);
    objc_release(v40);
    objc_release(v38);
  }
  j__objc_release(v17);
}
// 3E0FA4: using guessed type char *selRef_objectForKey_;
// 3E5CA8: using guessed type void *classRef_NSBundle;
// 3FADD8: using guessed type __CFString stru_3FADD8;
// 3FB0A8: using guessed type __CFString cfstr_Records;
// 3FB668: using guessed type __CFString cfstr_Nextpage;
// 3FB678: using guessed type __CFString cfstr_Size;
// 3FB688: using guessed type __CFString cfstr_Anchor;
// 3FDD08: using guessed type __CFString cfstr_Activityemptyc;

//----- (0006070C) --------------------------------------------------------
id __fastcall sub_6070C(int a1, int a2)
{
  return j__objc_retain(*(id *)(a2 + 20));
}

//----- (00060714) --------------------------------------------------------
void __fastcall sub_60714(int a1)
{
  j__objc_release(*(id *)(a1 + 20));
}

//----- (0006071C) --------------------------------------------------------
id __fastcall sub_6071C(int a1)
{
  *(_BYTE *)(*(_DWORD *)(a1 + 20) + 272) = 1;
  return j__objc_msgSend(*(id *)(a1 + 20), "stopLoading");
}

//----- (00060744) --------------------------------------------------------
id __fastcall sub_60744(int a1, int a2)
{
  return j__objc_retain(*(id *)(a2 + 20));
}

//----- (0006074C) --------------------------------------------------------
void __fastcall sub_6074C(int a1)
{
  j__objc_release(*(id *)(a1 + 20));
}

//----- (00060754) --------------------------------------------------------
id __fastcall sub_60754(int a1)
{
  *(_BYTE *)(*(_DWORD *)(a1 + 20) + 272) = 1;
  return j__objc_msgSend(*(id *)(a1 + 20), "stopLoading");
}

//----- (0006077C) --------------------------------------------------------
id __fastcall sub_6077C(int a1, int a2)
{
  return j__objc_retain(*(id *)(a2 + 20));
}

//----- (00060784) --------------------------------------------------------
void __fastcall sub_60784(int a1)
{
  j__objc_release(*(id *)(a1 + 20));
}

//----- (0005FCD8) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController tableView:didSelectRowAtIndexPath:](
        VNActivityTableViewController *self,
        SEL a2,
        id a3,
        id a4)
{
  id v5; // r4
  id v6; // r6

  v5 = objc_retain(a4);
  if ( self->_doesPaginate )
  {
    v6 = objc_msgSend(v5, "row");
    if ( v6 == objc_msgSend(self->_feed, "count") )
      -[VNActivityTableViewController load:size:addToExistingResults:](
        self,
        "load:size:addToExistingResults:",
        self->_nextPage,
        self->_nextSize,
        1);
  }
  j__objc_release(v5);
}

//----- (0005FD6C) --------------------------------------------------------
id __cdecl -[VNActivityTableViewController tableView:cellForRowAtIndexPath:](
        VNActivityTableViewController *self,
        SEL a2,
        id a3,
        id a4)
{
  id v5; // r8
  id v6; // r0
  id v7; // r4
  id v8; // r4
  id v9; // r0
  id v10; // r5
  id v11; // r0
  id v12; // r0
  id v13; // r5
  id v14; // r0
  id v15; // r6
  id v16; // r0
  NSMutableArray *feed; // r4
  id v18; // r0
  id v19; // r0
  id v20; // r0
  id v21; // r6
  id v22; // r0
  id v23; // r0
  id v24; // r8
  id v25; // r0
  id v26; // r6
  id v27; // r0
  NSMutableArray *attributedStrings; // r6
  id v29; // r0
  id v30; // r0
  id v31; // r6
  NSMutableArray *urls; // r5
  id v33; // r0
  id v34; // r0
  id v35; // r5
  id v37; // [sp+4h] [bp-20h]
  id v38; // [sp+8h] [bp-1Ch]

  v5 = objc_retain(a4);
  if ( (unsigned __int8)-[VNActivityTableViewController isEmpty](self, "isEmpty") )
  {
    v6 = -[VNTableViewController emptyCell](self, "emptyCell");
    v7 = objc_retainAutoreleasedReturnValue(v6);
  }
  else if ( self->_doesPaginate && (v8 = objc_msgSend(v5, "row"), v8 == objc_msgSend(self->_feed, "count")) )
  {
    v9 = objc_msgSend(self, "tableView");
    v10 = objc_retainAutoreleasedReturnValue(v9);
    v11 = objc_msgSend(v10, "dequeueReusableCellWithIdentifier:", CFSTR("VNLoadMoreCell"));
    v7 = objc_retainAutoreleasedReturnValue(v11);
    objc_release(v10);
    if ( !v7 )
    {
      v12 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
      v13 = objc_retainAutoreleasedReturnValue(v12);
      v14 = objc_msgSend(v13, "loadNibNamed:owner:options:", CFSTR("VNLoadMoreCell"), 0, 0);
      v15 = objc_retainAutoreleasedReturnValue(v14);
      v16 = objc_msgSend(v15, "objectAtIndex:", 0);
      v7 = objc_retainAutoreleasedReturnValue(v16);
      objc_release(v15);
      objc_release(v13);
    }
    objc_msgSend(v7, "setDisplaysMessage:", 1);
  }
  else
  {
    v38 = v5;
    feed = self->_feed;
    v18 = objc_msgSend(v5, "row");
    v19 = objc_msgSend(feed, "objectAtIndex:", v18);
    v37 = objc_retainAutoreleasedReturnValue(v19);
    v20 = objc_msgSend(self, "tableView");
    v21 = objc_retainAutoreleasedReturnValue(v20);
    v22 = objc_msgSend(v21, "dequeueReusableCellWithIdentifier:", CFSTR("VNActivityTableViewCell"));
    v7 = objc_retainAutoreleasedReturnValue(v22);
    objc_release(v21);
    if ( !v7 )
    {
      v23 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
      v24 = objc_retainAutoreleasedReturnValue(v23);
      v25 = objc_msgSend(v24, "loadNibNamed:owner:options:", CFSTR("VNActivityTableViewCell"), 0, 0);
      v26 = objc_retainAutoreleasedReturnValue(v25);
      v27 = objc_msgSend(v26, "objectAtIndex:", 0);
      v7 = objc_retainAutoreleasedReturnValue(v27);
      objc_release(v26);
      objc_release(v24);
    }
    v5 = v38;
    attributedStrings = self->_attributedStrings;
    v29 = objc_msgSend(v38, "row");
    v30 = objc_msgSend(attributedStrings, "objectAtIndex:", v29);
    v31 = objc_retainAutoreleasedReturnValue(v30);
    objc_msgSend(v7, "setMeta:", v31);
    objc_release(v31);
    urls = self->_urls;
    v33 = objc_msgSend(v38, "row");
    v34 = objc_msgSend(urls, "objectAtIndex:", v33);
    v35 = objc_retainAutoreleasedReturnValue(v34);
    objc_msgSend(v7, "setUrls:", v35);
    objc_release(v35);
    objc_msgSend(v7, "setRecord:", v37);
    objc_release(v37);
  }
  objc_release(v5);
  return j__objc_autoreleaseReturnValue(v7);
}
// 3E5CA8: using guessed type void *classRef_NSBundle;
// 3FB6B8: using guessed type __CFString cfstr_Vnloadmorecell;
// 3FDCF8: using guessed type __CFString cfstr_Vnactivitytabl_0;

//----- (00060084) --------------------------------------------------------
unsigned int __cdecl -[VNActivityTableViewController tableView:numberOfRowsInSection:](
        VNActivityTableViewController *self,
        SEL a2,
        id a3,
        int a4)
{
  unsigned __int8 v5; // r1
  unsigned int result; // r0
  int doesPaginate; // r5

  v5 = (unsigned __int8)-[VNActivityTableViewController isEmpty](self, "isEmpty", a3, a4);
  result = 1;
  if ( !v5 )
  {
    doesPaginate = (unsigned __int8)self->_doesPaginate;
    result = (unsigned int)objc_msgSend(self->_feed, "count");
    if ( doesPaginate )
      ++result;
  }
  return result;
}

//----- (000600DC) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController refresh](VNActivityTableViewController *self, SEL a2)
{
  objc_super v3; // [sp+0h] [bp-Ch] BYREF

  v3.receiver = self;
  v3.super_class = (Class)&OBJC_CLASS___VNActivityTableViewController;
  -[VNTableViewController refresh](&v3, "refresh");
  -[VNActivityTableViewController reload](self, "reload");
}
// 3E9410: using guessed type __objc2_class OBJC_CLASS___VNActivityTableViewController;

//----- (0006011C) --------------------------------------------------------
float __cdecl -[VNActivityTableViewController tableView:heightForRowAtIndexPath:](
        VNActivityTableViewController *self,
        SEL a2,
        id a3,
        id a4)
{
  float32x2_t v4; // d0
  id v6; // r8
  int32x2_t v7; // d16
  unsigned __int32 v8; // s16
  id v9; // r10
  NSMutableArray *attributedStrings; // r4
  id v11; // r0
  id v12; // r0
  const char *v13; // r0
  char *v14; // r5
  float32x2_t v15; // d16
  float32x2_t v16; // d8
  int v18; // [sp+0h] [bp-24h] BYREF
  float32_t v19; // [sp+4h] [bp-20h]

  v6 = objc_retain(a4);
  if ( (unsigned __int8)-[VNActivityTableViewController isEmpty](self, "isEmpty") )
  {
    v7.i32[0] = -[VNTableViewController emptyCellHeight](self, "emptyCellHeight");
    v7.i32[1] = v7.i32[0];
    v8 = vcvt_f32_s32(v7).u32[0];
  }
  else
  {
    v9 = objc_msgSend(v6, "row");
    if ( v9 >= objc_msgSend(self->_attributedStrings, "count") )
    {
      *(float *)&v8 = 61.0;
    }
    else
    {
      attributedStrings = self->_attributedStrings;
      v11 = objc_msgSend(v6, "row");
      v12 = objc_msgSend(attributedStrings, "objectAtIndex:", v11);
      v13 = (const char *)objc_retainAutoreleasedReturnValue(v12);
      v14 = (char *)v13;
      if ( v13 )
      {
        objc_msgSend_stret(&v18, v13, "frameSizeForWidth:", 1128923136);
        v15.f32[0] = 18.0;
        v15.f32[1] = 18.0;
        v4.f32[0] = v19;
        v16 = vadd_f32(v4, v15);
      }
      else
      {
        v16.f32[0] = 18.0;
        v16.f32[1] = 18.0;
        v19 = 0.0;
        v18 = 0;
      }
      objc_release(v14);
      v4.i32[0] = 1114898432;
      v8 = vmax_f32(v4, v16).u32[0];
    }
  }
  objc_release(v6);
  return *(float *)&v8;
}
// 601EC: variable 'v4' is possibly undefined

//----- (0005F4D0) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController dealloc](VNActivityTableViewController *self, SEL a2)
{
  VNInteractionManager *v3; // r0
  VNInteractionManager *v4; // r5
  objc_super v5; // [sp+0h] [bp-10h] BYREF

  v3 = +[VNInteractionManager sharedInstance](&OBJC_CLASS___VNInteractionManager, "sharedInstance");
  v4 = objc_retainAutoreleasedReturnValue(v3);
  -[VNInteractionManager removeNavigationListener:](v4, "removeNavigationListener:", self);
  objc_release(v4);
  v5.receiver = self;
  v5.super_class = (Class)&OBJC_CLASS___VNActivityTableViewController;
  -[VNTableViewController dealloc](&v5, "dealloc");
}
// 3E8E20: using guessed type __objc2_class OBJC_CLASS___VNInteractionManager;
// 3E9410: using guessed type __objc2_class OBJC_CLASS___VNActivityTableViewController;

//----- (0005F53C) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController stopLoading](VNActivityTableViewController *self, SEL a2)
{
  id v3; // r0
  id v4; // r5
  id v5; // r0
  id v6; // r5
  VNAPIManager *v7; // r0
  VNAPIManager *v8; // r6
  NSString *v9; // r0
  NSString *v10; // r5
  unsigned __int8 v11; // r4
  id v12; // r0
  id v13; // r5
  id v14; // r0
  id v15; // r6
  UIAccessibilityNotifications v16; // r10
  id v17; // r0
  VNAPIManager *v18; // r4
  id v19; // r0
  id v20; // r5
  id v21; // r0
  id v22; // r6
  VNAPIManager *v23; // r0
  objc_super v24; // [sp+4h] [bp-20h] BYREF

  if ( self->_activityRequestComplete )
  {
    v24.receiver = self;
    v24.super_class = (Class)&OBJC_CLASS___VNActivityTableViewController;
    -[PullRefreshTableViewController stopLoading](&v24, "stopLoading");
    objc_msgSend(self->_loaderView, "stopAnimating");
    v3 = objc_msgSend(self, "tableView");
    v4 = objc_retainAutoreleasedReturnValue(v3);
    objc_msgSend(v4, "setScrollEnabled:", 1);
    objc_release(v4);
    v5 = objc_msgSend(self, "tableView");
    v6 = objc_retainAutoreleasedReturnValue(v5);
    objc_msgSend(v6, "reloadData");
    objc_release(v6);
    v7 = +[VNAPIManager sharedInstance](&OBJC_CLASS___VNAPIManager, "sharedInstance");
    v8 = objc_retainAutoreleasedReturnValue(v7);
    v9 = -[VNAPIManager sessionKey](v8, "sessionKey");
    v10 = objc_retainAutoreleasedReturnValue(v9);
    if ( v10 )
    {
      v11 = (unsigned __int8)-[VNActivityTableViewController isEmpty](self, "isEmpty");
      objc_release(v10);
      objc_release(v8);
      if ( !v11 )
        return;
      v12 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
      v13 = objc_retainAutoreleasedReturnValue(v12);
      v14 = objc_msgSend(v13, "localizedStringForKey:value:table:", CFSTR("ActivityErrorLoading"), &stru_3FADD8, 0);
      v15 = objc_retainAutoreleasedReturnValue(v14);
      +[SVProgressHUD showErrorWithStatus:](&OBJC_CLASS___SVProgressHUD, "showErrorWithStatus:", v15);
      objc_release(v15);
      objc_release(v13);
      v16 = UIAccessibilityScreenChangedNotification;
      v17 = objc_msgSend(self, "tableView");
      v18 = (VNAPIManager *)objc_retainAutoreleasedReturnValue(v17);
      v19 = objc_msgSend(&OBJC_CLASS___NSIndexPath, "indexPathForRow:inSection:", 0, 0);
      v20 = objc_retainAutoreleasedReturnValue(v19);
      v21 = objc_msgSend(v18, "cellForRowAtIndexPath:", v20);
      v22 = objc_retainAutoreleasedReturnValue(v21);
      UIAccessibilityPostNotification(v16, v22);
      objc_release(v22);
      objc_release(v20);
      v23 = v18;
    }
    else
    {
      objc_release(0);
      v23 = v8;
    }
    objc_release(v23);
  }
}
// 3E5CA8: using guessed type void *classRef_NSBundle;
// 3E921C: using guessed type __objc2_class OBJC_CLASS___VNAPIManager;
// 3E9410: using guessed type __objc2_class OBJC_CLASS___VNActivityTableViewController;
// 3E9460: using guessed type __objc2_class OBJC_CLASS___SVProgressHUD;
// 3FADD8: using guessed type __CFString stru_3FADD8;
// 3FDCB8: using guessed type __CFString cfstr_Activityerrorl;

//----- (0005F784) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController rebuildMeta](VNActivityTableViewController *self, SEL a2)
{
  id v3; // r0
  NSMutableArray *v4; // r0
  NSMutableArray *attributedStrings; // r1
  id v6; // r0
  NSMutableArray *v7; // r0
  NSMutableArray *urls; // r1
  void *v9; // r8
  id v10; // r0
  id v11; // r5
  NSDictionary *v12; // r0
  NSDictionary *v13; // r0
  int v14; // r2
  id v15; // r0
  id v16; // r4
  id v17; // r0
  id v18; // r11
  void *v19; // r0
  id v20; // r0
  id v21; // r0
  id v22; // r4
  id v23; // r0
  id v24; // r5
  int v25; // r0
  id v26; // r0
  id v27; // r0
  id v28; // r4
  id v29; // r0
  id v30; // r5
  id v31; // r0
  NSDateFormatter *dateFormatter; // r4
  id v33; // r0
  id v34; // r5
  id v35; // r0
  id v36; // r6
  id v37; // r0
  id v38; // r4
  id v39; // r0
  id v40; // r8
  VNSimpleMarkupStyleManager *v41; // r0
  VNSimpleMarkupStyleManager *v42; // r4
  VNSimpleMarkup *v43; // r0
  VNSimpleMarkup *v44; // r5
  NSMutableArray *v45; // r4
  NSAttributedString *v46; // r0
  NSAttributedString *v47; // r6
  NSMutableArray *v48; // r10
  NSArray *v49; // r0
  NSArray *v50; // r6
  int v51; // [sp+20h] [bp-108h]
  id v53; // [sp+74h] [bp-B4h]
  NSMutableArray *obj; // [sp+78h] [bp-B0h]
  id v55; // [sp+7Ch] [bp-ACh]
  id v56; // [sp+80h] [bp-A8h]
  id v57; // [sp+84h] [bp-A4h]
  unsigned int i; // [sp+94h] [bp-94h]
  NSDictionary *v59; // [sp+98h] [bp-90h]
  int v60; // [sp+9Ch] [bp-8Ch] BYREF
  int v61; // [sp+A0h] [bp-88h]
  int v62; // [sp+A4h] [bp-84h] BYREF
  int v63; // [sp+A8h] [bp-80h]
  char v64[64]; // [sp+ACh] [bp-7Ch] BYREF
  __int64 v65; // [sp+ECh] [bp-3Ch] BYREF
  __int64 v66; // [sp+F4h] [bp-34h]
  __int64 v67; // [sp+FCh] [bp-2Ch]
  __int64 v68; // [sp+104h] [bp-24h]

  v3 = objc_msgSend(&OBJC_CLASS___NSMutableArray, "array");
  v4 = (NSMutableArray *)objc_retainAutoreleasedReturnValue(v3);
  attributedStrings = self->_attributedStrings;
  self->_attributedStrings = v4;
  objc_release(attributedStrings);
  v6 = objc_msgSend(&OBJC_CLASS___NSMutableArray, "array");
  v7 = (NSMutableArray *)objc_retainAutoreleasedReturnValue(v6);
  urls = self->_urls;
  self->_urls = v7;
  objc_release(urls);
  v67 = 0LL;
  v68 = 0LL;
  v65 = 0LL;
  v66 = 0LL;
  obj = objc_retain(self->_feed);
  v53 = objc_msgSend(obj, "countByEnumeratingWithState:objects:count:", &v65, v64, 16);
  if ( v53 )
  {
    v51 = *(_DWORD *)v66;
    do
    {
      for ( i = 0; i < (unsigned int)v53; ++i )
      {
        if ( *(_DWORD *)v66 != v51 )
          objc_enumerationMutation(obj);
        v9 = *(void **)(HIDWORD(v65) + 4 * i);
        v10 = objc_msgSend(v9, "objectForKeyedSubscript:", CFSTR("body"));
        v11 = objc_retainAutoreleasedReturnValue(v10);
        v12 = objc_msgSend(
                &OBJC_CLASS___NSDictionary,
                "dictionaryWithObjectsAndKeys:",
                CFSTR("user"),
                CFSTR("user"),
                CFSTR("16_Calibre-Regular_0-179-134"),
                CFSTR("mention"),
                CFSTR("16_Calibre-Regular_0-179-134"),
                CFSTR("tag"),
                0);
        v13 = objc_retainAutoreleasedReturnValue(v12);
        if ( !v11 )
        {
          v61 = 0;
          v63 = 0;
          v59 = v13;
          v60 = 0;
          v62 = 0;
LABEL_10:
          v15 = objc_msgSend(v9, "objectForKeyedSubscript:", CFSTR("entities"));
          v16 = objc_retainAutoreleasedReturnValue(v15);
          v17 = +[VNEntityFunctions markupString:withEntities:outerClass:format:offset:needsMarkup:](
                  &OBJC_CLASS___VNEntityFunctions,
                  "markupString:withEntities:outerClass:format:offset:needsMarkup:",
                  v11,
                  v16,
                  0,
                  v59,
                  0,
                  0);
          v18 = objc_retainAutoreleasedReturnValue(v17);
          objc_release(v11);
          v19 = v16;
          goto LABEL_13;
        }
        v59 = v13;
        objc_msgSend_stret(&v62, (SEL)v11, "rangeOfString:", CFSTR(": \""));
        if ( v63 )
        {
          v14 = v62;
        }
        else
        {
          objc_msgSend_stret(&v60, (SEL)v11, "rangeOfString:", CFSTR(", \""));
          v14 = v60;
          v63 = v61;
          v62 = v60;
          if ( !v61 )
            goto LABEL_10;
        }
        v20 = objc_msgSend(v11, "substringToIndex:", v14);
        v56 = objc_retainAutoreleasedReturnValue(v20);
        v21 = objc_msgSend(v11, "substringFromIndex:", v62);
        v22 = objc_retainAutoreleasedReturnValue(v21);
        v57 = v11;
        v23 = objc_msgSend(v9, "objectForKeyedSubscript:", CFSTR("entities"));
        v24 = objc_retainAutoreleasedReturnValue(v23);
        v25 = (int)objc_msgSend(v56, "length");
        v26 = +[VNEntityFunctions markupString:withEntities:outerClass:format:offset:](
                &OBJC_CLASS___VNEntityFunctions,
                "markupString:withEntities:outerClass:format:offset:",
                v22,
                v24,
                0,
                v59,
                -v25);
        v55 = objc_retainAutoreleasedReturnValue(v26);
        objc_release(v22);
        objc_release(v24);
        v27 = objc_msgSend(v9, "objectForKeyedSubscript:", CFSTR("entities"));
        v28 = objc_retainAutoreleasedReturnValue(v27);
        v29 = +[VNEntityFunctions markupString:withEntities:outerClass:format:offset:needsMarkup:](
                &OBJC_CLASS___VNEntityFunctions,
                "markupString:withEntities:outerClass:format:offset:needsMarkup:",
                v56,
                v28,
                0,
                v59,
                0,
                0);
        v30 = objc_retainAutoreleasedReturnValue(v29);
        objc_release(v56);
        objc_release(v28);
        v31 = objc_msgSend(v30, "stringByAppendingString:", v55);
        v18 = objc_retainAutoreleasedReturnValue(v31);
        objc_release(v57);
        objc_release(v55);
        v19 = v30;
LABEL_13:
        objc_release(v19);
        dateFormatter = self->_dateFormatter;
        v33 = objc_msgSend(v9, "objectForKey:", CFSTR("created"));
        v34 = objc_retainAutoreleasedReturnValue(v33);
        v35 = objc_msgSend(dateFormatter, "dateFromString:", v34);
        v36 = objc_retainAutoreleasedReturnValue(v35);
        v37 = objc_msgSend(v36, "longRelativeString");
        v38 = objc_retainAutoreleasedReturnValue(v37);
        v39 = objc_msgSend(
                v18,
                "stringByAppendingFormat:",
                CFSTR("\n<: activityTimestampNewLine :>\n<:><: grey :>%@<:>"),
                v38);
        v40 = objc_retainAutoreleasedReturnValue(v39);
        objc_release(v18);
        objc_release(v38);
        objc_release(v36);
        objc_release(v34);
        v41 = +[VNSimpleMarkupStyleManager sharedInstance](&OBJC_CLASS___VNSimpleMarkupStyleManager, "sharedInstance");
        v42 = objc_retainAutoreleasedReturnValue(v41);
        v43 = +[VNSimpleMarkup markupWithString:formatter:](
                &OBJC_CLASS___VNSimpleMarkup,
                "markupWithString:formatter:",
                v40,
                v42);
        v44 = objc_retainAutoreleasedReturnValue(v43);
        objc_release(v42);
        v45 = self->_attributedStrings;
        v46 = -[VNSimpleMarkup attributedString](v44, "attributedString");
        v47 = objc_retainAutoreleasedReturnValue(v46);
        objc_msgSend(v45, "addObject:", v47);
        objc_release(v47);
        v48 = self->_urls;
        v49 = -[VNSimpleMarkup userInfo](v44, "userInfo");
        v50 = objc_retainAutoreleasedReturnValue(v49);
        objc_msgSend(v48, "addObject:", v50);
        objc_release(v50);
        objc_release(v44);
        objc_release(v59);
        objc_release(v40);
      }
      v53 = objc_msgSend(obj, "countByEnumeratingWithState:objects:count:", &v65, v64, 16);
    }
    while ( v53 );
  }
  objc_release(obj);
}
// 3E9398: using guessed type __objc2_class OBJC_CLASS___VNSimpleMarkup;
// 3E93C0: using guessed type __objc2_class OBJC_CLASS___VNSimpleMarkupStyleManager;
// 3EA540: using guessed type __objc2_class OBJC_CLASS___VNEntityFunctions;
// 3FACA8: using guessed type __CFString cfstr_User;
// 3FB028: using guessed type __CFString cfstr_Entities;
// 3FB058: using guessed type __CFString cfstr_Mention;
// 3FB068: using guessed type __CFString cfstr_Tag;
// 3FB198: using guessed type __CFString cfstr_16CalibreRegul;
// 3FB318: using guessed type __CFString cfstr_Created;
// 3FC288: using guessed type __CFString cfstr_Activitytimest_0;
// 3FDCC8: using guessed type __CFString cfstr_Body;
// 3FDCD8: using guessed type __CFString stru_3FDCD8;
// 3FDCE8: using guessed type __CFString stru_3FDCE8;

void __cdecl -[VNActivityTableViewController viewWillAppear:](VNActivityTableViewController *self, SEL a2, char a3)
{
  VNInteractionManager *v4; // r0
  VNInteractionManager *v5; // r5
  objc_super v6; // [sp+0h] [bp-10h] BYREF

  v6.receiver = self;
  v6.super_class = (Class)&OBJC_CLASS___VNActivityTableViewController;
  objc_msgSendSuper2(&v6, "viewWillAppear:", a3);
  v4 = +[VNInteractionManager sharedInstance](&OBJC_CLASS___VNInteractionManager, "sharedInstance");
  v5 = objc_retainAutoreleasedReturnValue(v4);
  -[VNInteractionManager addNavigationListener:](v5, "addNavigationListener:", self);
  objc_release(v5);
  if ( !self->_feed && !(unsigned __int8)objc_msgSend(self->_loaderView, "isAnimating") )
  {
    objc_msgSend(self->_loaderView, "startAnimating");
    -[VNActivityTableViewController refresh](self, "refresh");
  }
}
// 3E8E20: using guessed type __objc2_class OBJC_CLASS___VNInteractionManager;
// 3E9410: using guessed type __objc2_class OBJC_CLASS___VNActivityTableViewController;

//----- (0005F488) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController viewWillDisappear:](VNActivityTableViewController *self, SEL a2, char a3)
{
  VNInteractionManager *v4; // r0
  VNInteractionManager *v5; // r5

  v4 = +[VNInteractionManager sharedInstance](&OBJC_CLASS___VNInteractionManager, "sharedInstance");
  v5 = objc_retainAutoreleasedReturnValue(v4);
  -[VNInteractionManager removeNavigationListener:](v5, "removeNavigationListener:", self);
  j__objc_release(v5);
}
// 3E8E20: using guessed type __objc2_class OBJC_CLASS___VNInteractionManager;

//----- (0005EF74) --------------------------------------------------------
VNActivityTableViewController *__cdecl -[VNActivityTableViewController initWithUserID:](
        VNActivityTableViewController *self,
        SEL a2,
        id a3)
{
  id v4; // r8
  VNActivityTableViewController *v5; // r0
  VNActivityTableViewController *v6; // r5
  NSString *v7; // r0
  NSString *v8; // r0
  NSString *endpoint; // r1
  NSDateFormatter *v10; // r0
  NSDateFormatter *v11; // r0
  NSDateFormatter *dateFormatter; // r1
  NSDateFormatter *v13; // r6
  NSTimeZone *v14; // r0
  NSTimeZone *v15; // r4
  objc_super v17; // [sp+0h] [bp-18h] BYREF

  v4 = objc_retain(a3);
  v17.receiver = self;
  v17.super_class = (Class)&OBJC_CLASS___VNActivityTableViewController;
  v5 = -[PullRefreshTableViewController initWithNibName:bundle:](
         &v17,
         "initWithNibName:bundle:",
         CFSTR("VNActivityTableViewController"),
         0);
  v6 = objc_retainAutoreleasedReturnValue(v5);
  objc_release(v6);
  if ( v6 )
  {
    v7 = objc_msgSend(&OBJC_CLASS___NSString, "stringWithFormat:", CFSTR("users/%@/notifications"), v4);
    v8 = objc_retainAutoreleasedReturnValue(v7);
    endpoint = v6->_endpoint;
    v6->_endpoint = v8;
    objc_release(endpoint);
    v10 = objc_msgSend(&OBJC_CLASS___NSDateFormatter, "alloc");
    v11 = objc_msgSend(v10, "init");
    dateFormatter = v6->_dateFormatter;
    v6->_dateFormatter = v11;
    objc_release(dateFormatter);
    objc_msgSend(v6->_dateFormatter, "setDateFormat:", CFSTR("yyyy-MM-dd'T'HH:mm:s.S"));
    v13 = v6->_dateFormatter;
    v14 = objc_msgSend(&OBJC_CLASS___NSTimeZone, "timeZoneWithAbbreviation:", CFSTR("UTC"));
    v15 = objc_retainAutoreleasedReturnValue(v14);
    objc_msgSend(v13, "setTimeZone:", v15);
    objc_release(v15);
  }
  objc_release(v4);
  return v6;
}
// 3E9410: using guessed type __objc2_class OBJC_CLASS___VNActivityTableViewController;
// 3FB1B8: using guessed type __CFString cfstr_YyyyMmDdTHhMmS;
// 3FB1C8: using guessed type __CFString cfstr_Utc;
// 3FDC98: using guessed type __CFString cfstr_Vnactivitytabl;
// 3FDCA8: using guessed type __CFString cfstr_UsersNotificat;

//----- (0005F0C4) --------------------------------------------------------
void __cdecl -[VNActivityTableViewController viewDidLoad](VNActivityTableViewController *self, SEL a2)
{
  id v3; // r0
  id v4; // r5
  id v5; // r0
  id v6; // r5
  id v7; // r0
  id v8; // r6
  id v9; // r0
  id v10; // r11
  UIView *v11; // r0
  UIView *v12; // r5
  id v13; // r0
  id v14; // r6
  VNLoaderView *v15; // r11
  id v16; // r0
  const char *v17; // r0
  char *v18; // r6
  VNLoaderView *v19; // r0
  VNLoaderView *loaderView; // r1
  id v21; // r0
  id v22; // r6
  id v23; // r0
  id v24; // r5
  id v25; // r0
  id v26; // r5
  id v27; // r0
  id v28; // r5
  id v29; // r0
  id v30; // r6
  CGRect v31; // [sp+10h] [bp-30h] BYREF
  objc_super v32; // [sp+20h] [bp-20h] BYREF

  v32.receiver = self;
  v32.super_class = (Class)&OBJC_CLASS___VNActivityTableViewController;
  -[VNTableViewController viewDidLoad](&v32, "viewDidLoad");
  v3 = objc_msgSend(self, "tableView");
  v4 = objc_retainAutoreleasedReturnValue(v3);
  objc_msgSend(v4, "setRowHeight:", 1112276992);
  objc_release(v4);
  v5 = objc_msgSend(self, "tableView");
  v6 = objc_retainAutoreleasedReturnValue(v5);
  v7 = objc_msgSend(&OBJC_CLASS___UIColor, "whiteColor");
  v8 = objc_retainAutoreleasedReturnValue(v7);
  objc_msgSend(v6, "setBackgroundColor:", v8);
  objc_release(v8);
  objc_release(v6);
  v9 = objc_msgSend(self, "tableView");
  v10 = objc_retainAutoreleasedReturnValue(v9);
  v11 = objc_msgSend(&OBJC_CLASS___UIView, "alloc");
  v12 = objc_msgSend(
          v11,
          "initWithFrame:",
          CGRectZero.origin.x,
          CGRectZero.origin.y,
          CGRectZero.size.width,
          CGRectZero.size.height);
  objc_msgSend(v10, "setTableFooterView:", v12);
  objc_release(v12);
  objc_release(v10);
  v13 = objc_msgSend(self, "tableView");
  v14 = objc_retainAutoreleasedReturnValue(v13);
  objc_msgSend(v14, "setSeparatorStyle:", 0);
  objc_release(v14);
  v15 = objc_msgSend(&OBJC_CLASS___VNLoaderView, "alloc");
  v16 = objc_msgSend(self, "view");
  v17 = (const char *)objc_retainAutoreleasedReturnValue(v16);
  v18 = (char *)v17;
  if ( v17 )
    objc_msgSend_stret(&v31, v17, "bounds");
  else
    memset(&v31, 0, sizeof(v31));
  v19 = -[VNLoaderView initWithFrame:](
          v15,
          "initWithFrame:",
          v31.origin.x,
          v31.origin.y,
          v31.size.width,
          v31.size.height);
  loaderView = self->_loaderView;
  self->_loaderView = v19;
  objc_release(loaderView);
  objc_release(v18);
  v21 = objc_msgSend(self, "view");
  v22 = objc_retainAutoreleasedReturnValue(v21);
  objc_msgSend(v22, "addSubview:", self->_loaderView);
  objc_release(v22);
  v23 = objc_msgSend(self, "view");
  v24 = objc_retainAutoreleasedReturnValue(v23);
  objc_msgSend(v24, "sendSubviewToBack:", self->_loaderView);
  objc_release(v24);
  objc_msgSend(self->_loaderView, "startAnimating");
  v25 = objc_msgSend(self, "tableView");
  v26 = objc_retainAutoreleasedReturnValue(v25);
  objc_msgSend(v26, "setScrollEnabled:", 0);
  objc_release(v26);
  v27 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
  v28 = objc_retainAutoreleasedReturnValue(v27);
  v29 = objc_msgSend(v28, "localizedStringForKey:value:table:", CFSTR("ActivityErrorLoading"), &stru_3FADD8, 0);
  v30 = objc_retainAutoreleasedReturnValue(v29);
  -[VNTableViewController setEmptyCellText:](self, "setEmptyCellText:", v30);
  objc_release(v30);
  objc_release(v28);
}
// 3E5CA8: using guessed type void *classRef_NSBundle;
// 3E9410: using guessed type __objc2_class OBJC_CLASS___VNActivityTableViewController;
// 3E9500: using guessed type __objc2_class OBJC_CLASS___VNLoaderView;
// 3FADD8: using guessed type __CFString stru_3FADD8;
// 3FDCB8: using guessed type __CFString cfstr_Activityerrorl;





//now to the CELL

//----- (0005ED6C) --------------------------------------------------------
NSDictionary *__cdecl -[VNActivityTableViewCell record](VNActivityTableViewCell *self, SEL a2)
{
  return self->_record;
}

//----- (0005ED7C) --------------------------------------------------------
TTTAttributedLabel *__cdecl -[VNActivityTableViewCell label](VNActivityTableViewCell *self, SEL a2)
{
  return self->_label;
}

//----- (0005ED8C) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setLabel:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  TTTAttributedLabel *v4; // r0
  TTTAttributedLabel *label; // r1

  v4 = (TTTAttributedLabel *)objc_retain(a3);
  label = self->_label;
  self->_label = v4;
  j__objc_release(label);
}

//----- (0005EDB4) --------------------------------------------------------
UIView *__cdecl -[VNActivityTableViewCell cellSeparatorView](VNActivityTableViewCell *self, SEL a2)
{
  return self->_cellSeparatorView;
}

//----- (0005EDC4) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setCellSeparatorView:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  UIView *v4; // r0
  UIView *cellSeparatorView; // r1

  v4 = (UIView *)objc_retain(a3);
  cellSeparatorView = self->_cellSeparatorView;
  self->_cellSeparatorView = v4;
  j__objc_release(cellSeparatorView);
}

//----- (0005EDEC) --------------------------------------------------------
NSAttributedString *__cdecl -[VNActivityTableViewCell meta](VNActivityTableViewCell *self, SEL a2)
{
  return self->_meta;
}

//----- (0005EDFC) --------------------------------------------------------
UIButton *__cdecl -[VNActivityTableViewCell vineThumb](VNActivityTableViewCell *self, SEL a2)
{
  return self->_vineThumb;
}

//----- (0005EE0C) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setVineThumb:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  UIButton *v4; // r0
  UIButton *vineThumb; // r1

  v4 = (UIButton *)objc_retain(a3);
  vineThumb = self->_vineThumb;
  self->_vineThumb = v4;
  j__objc_release(vineThumb);
}

//----- (0005EE34) --------------------------------------------------------
UIImageView *__cdecl -[VNActivityTableViewCell userFlag](VNActivityTableViewCell *self, SEL a2)
{
  return self->_userFlag;
}

//----- (0005EE44) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setUserFlag:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  UIImageView *v4; // r0
  UIImageView *userFlag; // r1

  v4 = (UIImageView *)objc_retain(a3);
  userFlag = self->_userFlag;
  self->_userFlag = v4;
  j__objc_release(userFlag);
}

//----- (0005EE6C) --------------------------------------------------------
UIButton *__cdecl -[VNActivityTableViewCell userThumb](VNActivityTableViewCell *self, SEL a2)
{
  return self->_userThumb;
}

//----- (0005EE7C) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setUserThumb:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  UIButton *v4; // r0
  UIButton *userThumb; // r1

  v4 = (UIButton *)objc_retain(a3);
  userThumb = self->_userThumb;
  self->_userThumb = v4;
  j__objc_release(userThumb);
}

//----- (0005EEA4) --------------------------------------------------------
NSArray *__cdecl -[VNActivityTableViewCell urls](VNActivityTableViewCell *self, SEL a2)
{
  return self->_urls;
}

//----- (0005EEB4) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell .cxx_destruct](VNActivityTableViewCell *self, SEL a2)
{
  objc_storeStrong((id *)&self->_urls, 0);
  objc_storeStrong((id *)&self->_userThumb, 0);
  objc_storeStrong((id *)&self->_userFlag, 0);
  objc_storeStrong((id *)&self->_vineThumb, 0);
  objc_storeStrong((id *)&self->_meta, 0);
  objc_storeStrong((id *)&self->_cellSeparatorView, 0);
  objc_storeStrong((id *)&self->_label, 0);
  objc_storeStrong((id *)&self->_record, 0);
  j__objc_storeStrong((id *)&self->_vineFlag, 0);
}

//----- (0005DE98) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell awakeFromNib](VNActivityTableViewCell *self, SEL a2)
{
  -[TTTAttributedLabel setLinkAttributes:](self->_label, "setLinkAttributes:", 0);
  -[TTTAttributedLabel setActiveLinkAttributes:](self->_label, "setActiveLinkAttributes:", 0);
  objc_msgSend(self->_label, "setNumberOfLines:", 0);
  -[TTTAttributedLabel setDelegate:](self->_label, "setDelegate:", self);
}

//----- (0005DF00) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setMeta:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  id v4; // r0
  NSAttributedString *v5; // r1
  NSAttributedString *meta; // r0
  TTTAttributedLabel *label; // r4
  int v8; // r8
  TTTAttributedLabel *v9; // r1
  int v10; // r3
  TTTAttributedLabel *v11; // r1
  TTTAttributedLabel *v12; // r4
  int v13; // r11
  TTTAttributedLabel *v14; // r1
  int v15; // r6
  TTTAttributedLabel *v16; // r1
  NSAttributedString *v17; // [sp+Ch] [bp-7Ch]
  __int64 v18; // [sp+10h] [bp-78h] BYREF
  __int64 v19; // [sp+18h] [bp-70h]
  int v20[4]; // [sp+20h] [bp-68h] BYREF
  int v21[4]; // [sp+30h] [bp-58h] BYREF
  __int64 v22; // [sp+40h] [bp-48h] BYREF
  __int64 v23; // [sp+48h] [bp-40h]
  int v24[4]; // [sp+50h] [bp-38h] BYREF
  int v25[10]; // [sp+60h] [bp-28h] BYREF

  v4 = objc_retain(a3);
  v5 = (NSAttributedString *)objc_retain(v4);
  meta = self->_meta;
  v17 = v5;
  self->_meta = v5;
  objc_release(meta);
  -[TTTAttributedLabel setText:](self->_label, "setText:", self->_meta);
  label = self->_label;
  if ( label )
  {
    objc_msgSend_stret(v25, (SEL)self->_label, "frame");
    v8 = v25[0];
    v9 = self->_label;
    if ( v9 )
    {
      objc_msgSend_stret(v24, (SEL)v9, "frame");
      v10 = v24[1];
      goto LABEL_6;
    }
  }
  else
  {
    v8 = 0;
    memset(v25, 0, 16);
  }
  v10 = 0;
  memset(v24, 0, sizeof(v24));
LABEL_6:
  objc_msgSend(label, "setFrame:", v8, v10, 1128923136, 0);
  objc_msgSend(self->_label, "sizeToFit");
  v11 = self->_label;
  if ( !v11 )
  {
    v22 = 0LL;
    v23 = 0LL;
    goto LABEL_10;
  }
  objc_msgSend_stret(&v22, (SEL)v11, "frame");
  if ( *((float *)&v23 + 1) < 44.0 )
  {
LABEL_10:
    v12 = self->_label;
    if ( v12 )
    {
      objc_msgSend_stret(v21, (SEL)self->_label, "frame");
      v13 = v21[0];
      v14 = self->_label;
      if ( v14 )
      {
        objc_msgSend_stret(v20, (SEL)v14, "frame");
        v15 = v20[1];
        v16 = self->_label;
        if ( v16 )
        {
          objc_msgSend_stret(&v18, (SEL)v16, "frame");
          objc_msgSend(v12, "setFrame:", v13, v15, (_DWORD)v19, 1110441984);
          goto LABEL_17;
        }
LABEL_16:
        v18 = 0LL;
        v19 = 0LL;
        objc_msgSend(v12, "setFrame:", v13, v15, 0, 1110441984);
        goto LABEL_17;
      }
    }
    else
    {
      v13 = 0;
      memset(v21, 0, sizeof(v21));
    }
    v15 = 0;
    memset(v20, 0, sizeof(v20));
    goto LABEL_16;
  }
LABEL_17:
  objc_release(v17);
}

//----- (0005E0B0) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setUrls:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  NSArray *urls; // r0
  id v5; // r6
  unsigned int i; // r5
  void *v7; // r4
  TTTAttributedLabel *label; // r10
  id v9; // r0
  id v10; // r11
  id v11; // r0
  char *v12; // r4
  void *v13; // [sp+4h] [bp-A4h]
  int v14; // [sp+Ch] [bp-9Ch]
  NSArray *obj; // [sp+20h] [bp-88h]
  int v17; // [sp+24h] [bp-84h] BYREF
  int v18; // [sp+28h] [bp-80h]
  char v19[64]; // [sp+2Ch] [bp-7Ch] BYREF
  __int64 v20; // [sp+6Ch] [bp-3Ch] BYREF
  __int64 v21; // [sp+74h] [bp-34h]
  __int64 v22; // [sp+7Ch] [bp-2Ch]
  __int64 v23; // [sp+84h] [bp-24h]

  v13 = &__stack_chk_guard;
  obj = (NSArray *)objc_retain(a3);
  urls = self->_urls;
  self->_urls = obj;
  objc_release(urls);
  v22 = 0LL;
  v23 = 0LL;
  v20 = 0LL;
  v21 = 0LL;
  v5 = objc_msgSend(obj, "countByEnumeratingWithState:objects:count:");
  if ( v5 )
  {
    v14 = *(_DWORD *)v21;
    do
    {
      for ( i = 0; i < (unsigned int)v5; ++i )
      {
        if ( *(_DWORD *)v21 != v14 )
          objc_enumerationMutation(obj);
        v7 = *(void **)(HIDWORD(v20) + 4 * i);
        label = self->_label;
        v9 = objc_msgSend(v7, "objectForKey:", CFSTR("object"));
        v10 = objc_retainAutoreleasedReturnValue(v9);
        v11 = objc_msgSend(v7, "objectForKey:", CFSTR("range"));
        v12 = (char *)objc_retainAutoreleasedReturnValue(v11);
        if ( v12 )
        {
          objc_msgSend_stret(&v17, v12, "rangeValue");
        }
        else
        {
          v18 = 0;
          v17 = 0;
        }
        -[TTTAttributedLabel addLinkToURL:withRange:](label, "addLinkToURL:withRange:", v10, v17, v18, v13);
        objc_release(v12);
        objc_release(v10);
      }
      v5 = objc_msgSend(obj, "countByEnumeratingWithState:objects:count:", &v20, v19, 16);
    }
    while ( v5 );
  }
}
// 5E1D4: variable 'v13' is possibly undefined
// 3FB2B8: using guessed type __CFString cfstr_Object;
// 3FB2C8: using guessed type __CFString cfstr_Range;
// 5E0B0: using guessed type char var_7C[64];

//----- (0005E218) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell vineThumbWasPressed:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  NSString *v4; // r0
  NSString *v5; // r5
  id v6; // r0
  id v7; // r6
  id v8; // r0
  id v9; // r4
  id v10; // r0
  id v11; // r8
  id v12; // r0
  id v13; // r5
  NSURL *v14; // r0
  NSURL *v15; // r4

  if ( !(unsigned __int8)objc_msgSend(self->_vineThumb, "isHidden", a3) )
  {
    v4 = objc_msgSend(&OBJC_CLASS___NSString, "stringWithFormat:", CFSTR("%@://post/"), CFSTR("vine"));
    v5 = objc_retainAutoreleasedReturnValue(v4);
    v6 = objc_msgSend(self->_record, "objectForKey:", CFSTR("postId"));
    v7 = objc_retainAutoreleasedReturnValue(v6);
    v8 = objc_msgSend(v7, "stringValue");
    v9 = objc_retainAutoreleasedReturnValue(v8);
    v10 = objc_msgSend(v5, "stringByAppendingString:", v9);
    v11 = objc_retainAutoreleasedReturnValue(v10);
    objc_release(v9);
    objc_release(v7);
    objc_release(v5);
    v12 = objc_msgSend(&OBJC_CLASS___UIApplication, "sharedApplication");
    v13 = objc_retainAutoreleasedReturnValue(v12);
    v14 = objc_msgSend(&OBJC_CLASS___NSURL, "URLWithString:", v11);
    v15 = objc_retainAutoreleasedReturnValue(v14);
    objc_msgSend(v13, "openURL:", v15);
    objc_release(v15);
    objc_release(v13);
    j__objc_release(v11);
  }
}
// 3E0FA4: using guessed type char *selRef_objectForKey_;
// 3E10F8: using guessed type char *selRef_stringValue;
// 3E5CC8: using guessed type void *classRef_NSString;
// 3FAC98: using guessed type __CFString cfstr_Vine;
// 3FB128: using guessed type __CFString cfstr_Postid;
// 3FDBD8: using guessed type __CFString cfstr_Post_2;

//----- (0005E374) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell userThumbWasPressed:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  NSString *v4; // r0
  NSString *v5; // r5
  id v6; // r0
  id v7; // r6
  id v8; // r0
  id v9; // r4
  id v10; // r0
  id v11; // r8
  id v12; // r0
  id v13; // r5
  NSURL *v14; // r0
  NSURL *v15; // r4

  v4 = objc_msgSend(&OBJC_CLASS___NSString, "stringWithFormat:", CFSTR("%@://user-id/"), CFSTR("vine"));
  v5 = objc_retainAutoreleasedReturnValue(v4);
  v6 = objc_msgSend(self->_record, "objectForKey:", CFSTR("userId"));
  v7 = objc_retainAutoreleasedReturnValue(v6);
  v8 = objc_msgSend(v7, "stringValue");
  v9 = objc_retainAutoreleasedReturnValue(v8);
  v10 = objc_msgSend(v5, "stringByAppendingString:", v9);
  v11 = objc_retainAutoreleasedReturnValue(v10);
  objc_release(v9);
  objc_release(v7);
  objc_release(v5);
  v12 = objc_msgSend(&OBJC_CLASS___UIApplication, "sharedApplication");
  v13 = objc_retainAutoreleasedReturnValue(v12);
  v14 = objc_msgSend(&OBJC_CLASS___NSURL, "URLWithString:", v11);
  v15 = objc_retainAutoreleasedReturnValue(v14);
  objc_msgSend(v13, "openURL:", v15);
  objc_release(v15);
  objc_release(v13);
  j__objc_release(v11);
}
// 3E0FA4: using guessed type char *selRef_objectForKey_;
// 3E10F8: using guessed type char *selRef_stringValue;
// 3E5CC8: using guessed type void *classRef_NSString;
// 3FAC98: using guessed type __CFString cfstr_Vine;
// 3FB0D8: using guessed type __CFString cfstr_Userid;
// 3FB208: using guessed type __CFString cfstr_UserId;

//----- (0005E4A8) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell attributedLabel:didSelectLinkWithURL:](
        VNActivityTableViewCell *self,
        SEL a2,
        id a3,
        id a4)
{
  id v4; // r4
  id v5; // r0
  id v6; // r5

  v4 = objc_retain(a4);
  sub_21AC34(
    (int)CFSTR("%s line %d $ Activity cell link tapped: %@"),
    "-[VNActivityTableViewCell attributedLabel:didSelectLinkWithURL:]",
    53,
    v4);
  v5 = objc_msgSend(&OBJC_CLASS___UIApplication, "sharedApplication");
  v6 = objc_retainAutoreleasedReturnValue(v5);
  objc_msgSend(v6, "openURL:", v4);
  objc_release(v4);
  j__objc_release(v6);
}
// 3FDBE8: using guessed type __CFString cfstr_SLineDActivity;

//----- (0005E518) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setRecord:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  id v4; // r0
  NSDictionary *v5; // r1
  NSDictionary *record; // r0
  VNActivityTableViewCell *v7; // r11
  UIButton *userThumb; // r10
  id v9; // r0
  id v10; // r4
  id v11; // r0
  id v12; // r5
  id v13; // r0
  id v14; // r6
  id v15; // r0
  id v16; // r5
  id v17; // r0
  id v18; // r6
  id v19; // r0
  id v20; // r5
  _BOOL4 v21; // r11
  id v22; // r0
  id v23; // r6
  NSDictionary *v24; // r8
  id v25; // r0
  id v26; // r5
  id v27; // r0
  id v28; // r4
  id v29; // r0
  id v30; // r4
  id v31; // r0
  id v32; // r6
  void *v33; // r10
  id v34; // r0
  id v35; // r4
  id v36; // r0
  const char *v37; // r0
  char *v38; // r8
  UIButton *v39; // r10
  id v40; // r0
  id v41; // r6
  NSURL *v42; // r0
  NSURL *v43; // r5
  UIButton *v44; // r4
  id v45; // r0
  id v46; // r5
  id v47; // r0
  NSDictionary *v48; // r11
  id v49; // r8
  id v50; // r0
  id v51; // r6
  _BOOL4 v52; // r5
  id v53; // r0
  id v54; // r4
  id v55; // r5
  VNActivityTableViewCell *v56; // r6
  UIButton *v57; // r0
  UIButton *v58; // r8
  id v59; // r0
  id v60; // r6
  NSURL *v61; // r0
  NSURL *v62; // r5
  void *v63; // r0
  UIImageView *v64; // r0
  VNActivityTableViewCell *v65; // r4
  UIImageView *v66; // r6
  VNActivityTableViewCell *v67; // r6
  UIImageView *v68; // r0
  UIImageView *v69; // r4
  id v70; // r0
  id v71; // r5
  id v72; // r4
  UIImageView *v73; // r0
  UIImageView *v74; // r4
  UIImageView *v75; // r0
  UIImageView *v76; // r0
  UIImageView *v77; // r0
  UIImageView *v78; // r4
  UIButton *v79; // r0
  id v80; // r0
  id v81; // r5
  UIButton *vineThumb; // [sp+4h] [bp-44h]
  UIButton *v83; // [sp+Ch] [bp-3Ch]
  NSDictionary *v84; // [sp+10h] [bp-38h]
  UIButton *v85; // [sp+14h] [bp-34h]
  int v87; // [sp+28h] [bp-20h] BYREF
  int v88; // [sp+2Ch] [bp-1Ch]

  v4 = objc_retain(a3);
  v5 = (NSDictionary *)objc_retain(v4);
  record = self->_record;
  v84 = v5;
  self->_record = v5;
  objc_release(record);
  v7 = self;
  userThumb = self->_userThumb;
  v9 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
  v10 = objc_retainAutoreleasedReturnValue(v9);
  v11 = objc_msgSend(v10, "localizedStringForKey:value:table:", CFSTR("AccessibilityActivityLabelUserThumb"));
  v12 = objc_retainAutoreleasedReturnValue(v11);
  objc_msgSend(userThumb, "setAccessibilityLabel:", v12);
  objc_release(v12);
  objc_release(v10);
  v85 = v7->_userThumb;
  v13 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
  v14 = objc_retainAutoreleasedReturnValue(v13);
  v15 = objc_msgSend(
          v14,
          "localizedStringForKey:value:table:",
          CFSTR("AccessibilityActivityHintUserThumb"),
          &stru_3FADD8,
          0);
  v16 = objc_retainAutoreleasedReturnValue(v15);
  objc_msgSend(v85, "setAccessibilityHint:", v16);
  objc_release(v16);
  objc_release(v14);
  vineThumb = self->_vineThumb;
  v17 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
  v18 = objc_retainAutoreleasedReturnValue(v17);
  v19 = objc_msgSend(
          v18,
          "localizedStringForKey:value:table:",
          CFSTR("AccessibilityActivityLabelVineThumb"),
          &stru_3FADD8,
          0);
  v20 = objc_retainAutoreleasedReturnValue(v19);
  objc_msgSend(vineThumb, "setAccessibilityLabel:", v20);
  objc_release(v20);
  objc_release(v18);
  v83 = self->_vineThumb;
  v21 = 0;
  v22 = objc_msgSend(&OBJC_CLASS___NSBundle, "mainBundle");
  v23 = objc_retainAutoreleasedReturnValue(v22);
  v24 = v84;
  v25 = objc_msgSend(
          v23,
          "localizedStringForKey:value:table:",
          CFSTR("AccessibilityActivityHintVineThumb"),
          &stru_3FADD8,
          0);
  v26 = objc_retainAutoreleasedReturnValue(v25);
  objc_msgSend(v83, "setAccessibilityHint:", v26);
  objc_release(v26);
  objc_release(v23);
  v27 = objc_msgSend(self->_userThumb, "imageView");
  v28 = objc_retainAutoreleasedReturnValue(v27);
  objc_msgSend(v28, "setContentMode:", 2);
  objc_release(v28);
  v29 = objc_msgSend(v84, "objectForKey:", CFSTR("avatarUrl"));
  v30 = objc_retainAutoreleasedReturnValue(v29);
  v31 = objc_msgSend(&OBJC_CLASS___NSNull, "null");
  v32 = objc_retainAutoreleasedReturnValue(v31);
  v33 = v30;
  if ( v30 != v32 )
  {
    v34 = objc_msgSend(v84, "objectForKey:", CFSTR("avatarUrl"));
    v35 = objc_retainAutoreleasedReturnValue(v34);
    v21 = 0;
    if ( objc_msgSend(v35, "length") )
    {
      v36 = objc_msgSend(v84, "objectForKeyedSubscript:", CFSTR("avatarUrl"));
      v37 = (const char *)objc_retainAutoreleasedReturnValue(v36);
      v38 = (char *)v37;
      if ( v37 )
      {
        objc_msgSend_stret(&v87, v37, "rangeOfString:", CFSTR("default"));
        v21 = v88 == 0;
      }
      else
      {
        v21 = 1;
        v88 = 0;
        v87 = 0;
      }
      objc_release(v38);
      v24 = v84;
    }
    objc_release(v35);
  }
  objc_release(v32);
  objc_release(v33);
  v39 = self->_userThumb;
  if ( v21 )
  {
    v40 = objc_msgSend(v24, "objectForKey:", CFSTR("avatarUrl"));
    v41 = objc_retainAutoreleasedReturnValue(v40);
    v42 = objc_msgSend(&OBJC_CLASS___NSURL, "URLWithString:", v41);
    v43 = objc_retainAutoreleasedReturnValue(v42);
    objc_msgSend(v39, "setImageWithURL:", v43);
    objc_release(v43);
    objc_release(v41);
  }
  else
  {
    objc_msgSend(self->_userThumb, "cancelImageRequestOperation");
    v44 = self->_userThumb;
    v45 = objc_msgSend(&OBJC_CLASS___UIImage, "imageNamed:", CFSTR("BlankAvatar"));
    v46 = objc_retainAutoreleasedReturnValue(v45);
    objc_msgSend(v44, "setImage:forState:", v46, 0);
    objc_release(v46);
  }
  v47 = objc_msgSend(v24, "objectForKey:", CFSTR("thumbnailUrl"));
  v48 = v24;
  v49 = objc_retainAutoreleasedReturnValue(v47);
  v50 = objc_msgSend(&OBJC_CLASS___NSNull, "null");
  v51 = objc_retainAutoreleasedReturnValue(v50);
  v52 = 0;
  if ( v49 != v51 )
  {
    v53 = objc_msgSend(v48, "objectForKey:", CFSTR("thumbnailUrl"));
    v54 = objc_retainAutoreleasedReturnValue(v53);
    v55 = objc_msgSend(v54, "length");
    objc_release(v54);
    v52 = v55 != 0;
  }
  objc_release(v51);
  objc_release(v49);
  v56 = self;
  v57 = self->_vineThumb;
  if ( v52 )
  {
    objc_msgSend(v57, "setHidden:", 0);
    v58 = self->_vineThumb;
    v59 = objc_msgSend(v48, "objectForKey:", CFSTR("thumbnailUrl"));
    v60 = objc_retainAutoreleasedReturnValue(v59);
    v61 = objc_msgSend(&OBJC_CLASS___NSURL, "URLWithString:", v60);
    v62 = objc_retainAutoreleasedReturnValue(v61);
    objc_msgSend(v58, "setImageWithURL:", v62);
    objc_release(v62);
    v63 = v60;
    v56 = self;
    objc_release(v63);
  }
  else
  {
    objc_msgSend(v57, "cancelImageRequestOperation");
    objc_msgSend(self->_vineThumb, "setHidden:", 1);
  }
  v64 = -[VNActivityTableViewCell userFlag](v56, "userFlag");
  v65 = v56;
  v66 = objc_retainAutoreleasedReturnValue(v64);
  objc_msgSend(v66, "setHidden:", 1);
  objc_release(v66);
  v67 = v65;
  v68 = -[VNActivityTableViewCell vineFlag](v65, "vineFlag");
  v69 = objc_retainAutoreleasedReturnValue(v68);
  objc_msgSend(v69, "setHidden:", 1);
  objc_release(v69);
  v70 = objc_msgSend(v48, "objectForKey:", CFSTR("notificationTypeId"));
  v71 = objc_retainAutoreleasedReturnValue(v70);
  v72 = objc_msgSend(v71, "intValue");
  objc_release(v71);
  switch ( (unsigned int)v72 )
  {
    case 1u:
    case 5u:
      v75 = -[VNActivityTableViewCell userFlag](v67, "userFlag");
      v74 = objc_retainAutoreleasedReturnValue(v75);
      -[VNActivityTableViewCell setFlag:imageName:](v67, "setFlag:imageName:", v74, CFSTR("AddPhotoCorner"));
      goto LABEL_20;
    case 2u:
      v76 = -[VNActivityTableViewCell vineFlag](v67, "vineFlag");
      v74 = objc_retainAutoreleasedReturnValue(v76);
      -[VNActivityTableViewCell setFlag:imageName:](v67, "setFlag:imageName:", v74, CFSTR("LikePhotoCorner"));
      goto LABEL_20;
    case 3u:
    case 4u:
    case 7u:
    case 8u:
    case 9u:
    case 0xAu:
    case 0xBu:
      v73 = -[VNActivityTableViewCell vineFlag](v67, "vineFlag");
      v74 = objc_retainAutoreleasedReturnValue(v73);
      -[VNActivityTableViewCell setFlag:imageName:](v67, "setFlag:imageName:", v74, CFSTR("CommentPhotoCorner"));
      goto LABEL_20;
    case 6u:
      v77 = -[VNActivityTableViewCell vineFlag](v67, "vineFlag");
      v78 = objc_retainAutoreleasedReturnValue(v77);
      -[VNActivityTableViewCell setFlag:imageName:](v67, "setFlag:imageName:", v78, CFSTR("BlockedPhotoCorner"));
      objc_release(v78);
      v79 = -[VNActivityTableViewCell userThumb](v67, "userThumb");
      v74 = objc_retainAutoreleasedReturnValue(v79);
      v80 = objc_msgSend(&OBJC_CLASS___UIImage, "imageNamed:", CFSTR("AdminProfilePhoto"));
      v81 = objc_retainAutoreleasedReturnValue(v80);
      objc_msgSend(v74, "setImage:forState:", v81, 0);
      objc_release(v81);
LABEL_20:
      objc_release(v74);
      break;
    default:
      break;
  }
  objc_release(v48);
}
// 3E5CA8: using guessed type void *classRef_NSBundle;
// 3FADD8: using guessed type __CFString stru_3FADD8;
// 3FB2D8: using guessed type __CFString cfstr_Avatarurl;
// 3FB2E8: using guessed type __CFString cfstr_Default;
// 3FB2F8: using guessed type __CFString cfstr_Blankavatar;
// 3FB338: using guessed type __CFString cfstr_Thumbnailurl;
// 3FDBF8: using guessed type __CFString cfstr_Accessibilitya;
// 3FDC08: using guessed type __CFString cfstr_Accessibilitya_0;
// 3FDC18: using guessed type __CFString cfstr_Accessibilitya_1;
// 3FDC28: using guessed type __CFString cfstr_Accessibilitya_2;
// 3FDC38: using guessed type __CFString cfstr_Notificationty;
// 3FDC48: using guessed type __CFString cfstr_Addphotocorner;
// 3FDC58: using guessed type __CFString cfstr_Likephotocorne;
// 3FDC68: using guessed type __CFString cfstr_Commentphotoco;
// 3FDC78: using guessed type __CFString cfstr_Blockedphotoco;
// 3FDC88: using guessed type __CFString cfstr_Adminprofileph;

//----- (0005EC34) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setFlag:imageName:](VNActivityTableViewCell *self, SEL a2, id a3, id a4)
{
  id v6; // r5
  id v7; // r0
  id v8; // r6

  v6 = objc_retain(a3);
  v7 = objc_msgSend(&OBJC_CLASS___UIImage, "imageNamed:", a4);
  v8 = objc_retainAutoreleasedReturnValue(v7);
  objc_msgSend(a3, "setImage:", v8);
  objc_release(v8);
  objc_msgSend(a3, "setHidden:", 0);
  j__objc_release(v6);
}

//----- (0005ECA4) --------------------------------------------------------
id __cdecl -[VNActivityTableViewCell accessibilityLabel](VNActivityTableViewCell *self, SEL a2)
{
  return j__objc_msgSend(self->_label, "text");
}

//----- (0005ECC4) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell layoutSubviews](VNActivityTableViewCell *self, SEL a2)
{
  UIView *cellSeparatorView; // r4
  float32x2_t v4; // d16
  float32x2_t v5; // d17
  objc_super v6; // [sp+0h] [bp-10h] BYREF

  v6.receiver = self;
  v6.super_class = (Class)&OBJC_CLASS___VNActivityTableViewCell;
  objc_msgSendSuper2(&v6, "layoutSubviews");
  cellSeparatorView = self->_cellSeparatorView;
  v4.f32[0] = -1.0;
  v4.f32[1] = -1.0;
  v5.i32[0] = (__int32)objc_msgSend(self, "height");
  v5.i32[1] = v5.i32[0];
  objc_msgSend(cellSeparatorView, "setY:", vadd_f32(v5, v4).u32[0]);
}
// 3E93E8: using guessed type __objc2_class OBJC_CLASS___VNActivityTableViewCell;

//----- (0005ED34) --------------------------------------------------------
UIImageView *__cdecl -[VNActivityTableViewCell vineFlag](VNActivityTableViewCell *self, SEL a2)
{
  return self->_vineFlag;
}

//----- (0005ED44) --------------------------------------------------------
void __cdecl -[VNActivityTableViewCell setVineFlag:](VNActivityTableViewCell *self, SEL a2, id a3)
{
  UIImageView *v4; // r0
  UIImageView *vineFlag; // r1

  v4 = (UIImageView *)objc_retain(a3);
  vineFlag = self->_vineFlag;
  self->_vineFlag = v4;
  j__objc_release(vineFlag);
}